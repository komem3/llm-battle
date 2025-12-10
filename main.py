from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.agents.middleware import ModelRetryMiddleware
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.typing import InputT
from getpass import getpass
from langchain_anthropic import ChatAnthropic
import os
import asyncio
import csv

if "ANTHROPIC_API_KEY" not in os.environ:
    os.environ["ANTHROPIC_API_KEY"] = getpass()

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass()

themes = (
    ("人間の本質は『善』か『悪（利己的）』か", ("善", "悪")),
    ("数学は「発見」されたのか、「発明」されたのか", ("発見", "発明")),
    (
        "「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？）",
        ("同じ", "異なる"),
    ),
    ("辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？", ("真実", "幸福")),
)


class ChatResponse(BaseModel):
    content: str = Field(description="チャットのレスポンス")
    stop: bool = Field(description="議論に明確な結論がでたかどうか")


class JudgeResponse(BaseModel):
    content: str = Field(description="判定内容の説明")
    winner: int = Field(description="勝者")


class Agent:
    def __init__(self, model_name: str, response_format: ToolStrategy):
        if "gemini" in model_name:
            self.agent = create_agent(
                model=ChatVertexAI(
                    model=model_name,
                    location="global",
                ),
                response_format=response_format,
                middleware=[
                    ModelRetryMiddleware(
                        max_retries=5,
                        backoff_factor=2.0,
                        initial_delay=1.0,
                        retry_on=self.should_retry,
                        on_failure=self.format_error,
                    ),
                ],
            )
        if "claude" in model_name:
            self.agent = create_agent(
                model=ChatAnthropic(
                    model=model_name,
                ),
                response_format=response_format,
                middleware=[
                    ModelRetryMiddleware(
                        max_retries=5,
                        backoff_factor=2.0,
                        initial_delay=1.0,
                        retry_on=self.should_retry,
                        on_failure=self.format_error,
                    ),
                ],
            )
        if "gpt" in model_name:
            self.agent = create_agent(
                model=model_name,
                response_format=response_format,
                middleware=[
                    ModelRetryMiddleware(
                        max_retries=5,
                        backoff_factor=4.0,
                        initial_delay=5.0,
                        retry_on=self.should_retry,
                        on_failure=self.format_error,
                    ),
                ],
            )
        self.model_name = model_name
        self.error_count = 0

    def format_error(self, error: Exception) -> str:
        return f"Model call failed: {error}. Please try again later."

    def should_retry(self, error: Exception) -> bool:
        self.error_count += 1
        # Only retry on rate limit errors
        if isinstance(error, TimeoutError):
            print(f"({self.error_count}) {self.model_name} occur timeout. retry...")
            return True
        # Or check for specific HTTP status codes
        if hasattr(error, "status_code"):
            print(f"({self.error_count}) {self.model_name} occur api quate. retry...")
            return error.status_code in (429, 503)

        print(f"{self.model_name} occur no retry error.")
        return False

    def get_name(self):
        return self.model_name

    def __str__(self):
        return self.get_name()

    def invoke(self, input: InputT):
        self.error_count = 0
        return self.agent.ainvoke(input)


async def debate(
    theme: str,
    sides: tuple[str, str],
    players: tuple[Agent, Agent],
    judger: Agent,
    csv_writer,
):
    print(
        f"write to 'outputs/{theme}_({sides[0]}|{sides[1]})_{players[0]}_{players[1]}.md'"
    )
    with open(
        f"outputs/{theme}_({sides[0]}|{sides[1]})_{players[0]}_{players[1]}.md", "w"
    ) as f:
        player1_messages = [
            SystemMessage(
                content=f"{theme}について議論しています。あなたは{sides[0]}を主張してください。"
            ),
            HumanMessage(content="あなたの主張を教えてください。"),
        ]
        player2_messages = [
            SystemMessage(
                content=f"{theme}について議論しています。あなたは{sides[1]}を主張してください。また議論に明確な結論が出たと感じたらstopしてください。"
            ),
        ]
        messages = [
            HumanMessage(
                content=f"以下に記載するのは{theme}についての異なる主張の口論です。この履歴からどちらがこの議論で勝利を収めたかを判定してください。必ず勝敗を付けてください。winnerは{sides[0]}が勝った場合は0、{sides[1]}が勝った場合は1として下さい"
            )
        ]
        for i in range(10):
            f.write(f"\n# {players[0]}({sides[0]}派)\n")
            response = await players[0].invoke({"messages": player1_messages})
            if "structured_response" not in response:
                print(f"{players[0]} response not structured\n{response}")
            f.write(f"{response['structured_response'].content}\n")
            player1_messages.append(
                AIMessage(content=response["structured_response"].content)
            )
            player2_messages.append(
                HumanMessage(content=response["structured_response"].content)
            )

            messages.append(
                HumanMessage(
                    content=f"---- {players[0]}({sides[0]}派) ----\n{response['structured_response'].content}"
                )
            )

            f.write(f"\n# {players[1]}({sides[1]}派)\n")
            response = await players[1].invoke({"messages": player2_messages})
            if "structured_response" not in response:
                print(f"{players[1]} response not structured\n{response}")

            f.write(f"{response['structured_response'].content}\n")
            player2_messages.append(
                AIMessage(content=response["structured_response"].content)
            )
            player1_messages.append(
                HumanMessage(content=response["structured_response"].content)
            )
            messages.append(
                HumanMessage(
                    content=f"---- {players[1]}({sides[1]}派) ----\n{response['structured_response'].content}"
                )
            )

            if response["structured_response"].stop:
                break
        result = await judger.invoke({"messages": messages})
        f.write("\n--- result ---\n")
        f.write(f"{result['structured_response'].content}\n")

    print(
        f"{theme}: {players[0]}({sides[0]}) vs {players[1]}({sides[1]}) → winner: {players[result['structured_response'].winner]}"
    )
    csv_writer.writerow(
        [
            theme,
            sides[0],
            sides[1],
            players[0].get_name(),
            players[1].get_name(),
            result["structured_response"].winner,
            judger.get_name(),
        ]
    )
    return result["structured_response"].winner


async def compare_model():
    gemini = Agent(
        "gemini-3-pro-preview",
        response_format=ChatResponse,
    )
    claude = Agent(
        "claude-opus-4-5",
        response_format=ChatResponse,
    )
    gpt = Agent(
        "gpt-5.1",
        response_format=ChatResponse,
    )
    judger = Agent(
        "gemini-3-pro-preview",
        response_format=ToolStrategy(JudgeResponse),
    )

    with open("result.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            ["theme", "side1", "side2", "player1", "player2", "winner", "judger"]
        )
        for theme in themes:
            tasks = []
            for pattern in ((gemini, claude), (gemini, gpt), (gpt, claude)):
                tasks.extend(
                    [
                        debate(theme[0], theme[1], pattern, judger, csv_writer),
                        debate(
                            theme[0],
                            tuple(reversed(theme[1])),
                            pattern,
                            judger,
                            csv_writer,
                        ),
                        debate(
                            theme[0],
                            theme[1],
                            tuple(reversed(pattern)),
                            judger,
                            csv_writer,
                        ),
                        debate(
                            theme[0],
                            tuple(reversed(theme[1])),
                            tuple(reversed(pattern)),
                            judger,
                            csv_writer,
                        ),
                    ]
                )
            await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(compare_model())
