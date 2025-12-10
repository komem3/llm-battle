# LLM Battle

LLM 同士をレスバさせて勝敗を決めることで、LLMの性能を比較してみた。

## 結果

### 詳細

<details>
<summary>結果一覧</summary>

|                             テーマ                             |            サイド1            |            サイド2            |         勝者         |
| :------------------------------------------------------------: | :---------------------------: | :---------------------------: | :------------------: |
|             人間の本質は『善』か『悪（利己的）』か             |     claude-opus-4-5 (悪)      |   gemini-3-pro-preview (善)   |   claude-opus-4-5    |
|             人間の本質は『善』か『悪（利己的）』か             |     claude-opus-4-5 (善)      |         gpt-5.1 (悪)          |       gpt-5.1        |
|             人間の本質は『善』か『悪（利己的）』か             |   gemini-3-pro-preview (善)   |     claude-opus-4-5 (悪)      |   claude-opus-4-5    |
|             人間の本質は『善』か『悪（利己的）』か             |     claude-opus-4-5 (善)      |   gemini-3-pro-preview (悪)   |   claude-opus-4-5    |
|             人間の本質は『善』か『悪（利己的）』か             |   gemini-3-pro-preview (善)   |         gpt-5.1 (悪)          |       gpt-5.1        |
|             人間の本質は『善』か『悪（利己的）』か             |   gemini-3-pro-preview (悪)   |     claude-opus-4-5 (善)      |   claude-opus-4-5    |
|             人間の本質は『善』か『悪（利己的）』か             |   gemini-3-pro-preview (悪)   |         gpt-5.1 (善)          |       gpt-5.1        |
|             人間の本質は『善』か『悪（利己的）』か             |         gpt-5.1 (善)          |   gemini-3-pro-preview (悪)   |       gpt-5.1        |
|             人間の本質は『善』か『悪（利己的）』か             |     claude-opus-4-5 (悪)      |         gpt-5.1 (善)          |       gpt-5.1        |
|             人間の本質は『善』か『悪（利己的）』か             |         gpt-5.1 (善)          |     claude-opus-4-5 (悪)      |       gpt-5.1        |
|             人間の本質は『善』か『悪（利己的）』か             |         gpt-5.1 (悪)          |     claude-opus-4-5 (善)      |       gpt-5.1        |
|             人間の本質は『善』か『悪（利己的）』か             |         gpt-5.1 (悪)          |   gemini-3-pro-preview (善)   | gemini-3-pro-preview |
|          数学は「発見」されたのか、「発明」されたのか          |    claude-opus-4-5 (発見)     |  gemini-3-pro-preview (発明)  |   claude-opus-4-5    |
|          数学は「発見」されたのか、「発明」されたのか          |  gemini-3-pro-preview (発明)  |        gpt-5.1 (発見)         |       gpt-5.1        |
|          数学は「発見」されたのか、「発明」されたのか          |    claude-opus-4-5 (発明)     |  gemini-3-pro-preview (発見)  |   claude-opus-4-5    |
|          数学は「発見」されたのか、「発明」されたのか          |        gpt-5.1 (発明)         |  gemini-3-pro-preview (発見)  |       gpt-5.1        |
|          数学は「発見」されたのか、「発明」されたのか          |  gemini-3-pro-preview (発見)  |    claude-opus-4-5 (発明)     | gemini-3-pro-preview |
|          数学は「発見」されたのか、「発明」されたのか          |    claude-opus-4-5 (発見)     |        gpt-5.1 (発明)         |   claude-opus-4-5    |
|          数学は「発見」されたのか、「発明」されたのか          |    claude-opus-4-5 (発明)     |        gpt-5.1 (発見)         |   claude-opus-4-5    |
|          数学は「発見」されたのか、「発明」されたのか          |  gemini-3-pro-preview (発見)  |        gpt-5.1 (発明)         |       gpt-5.1        |
|          数学は「発見」されたのか、「発明」されたのか          |  gemini-3-pro-preview (発明)  |    claude-opus-4-5 (発見)     |   claude-opus-4-5    |
|          数学は「発見」されたのか、「発明」されたのか          |        gpt-5.1 (発見)         |    claude-opus-4-5 (発明)     |       gpt-5.1        |
|          数学は「発見」されたのか、「発明」されたのか          |        gpt-5.1 (発明)         |    claude-opus-4-5 (発見)     |       gpt-5.1        |
|          数学は「発見」されたのか、「発明」されたのか          |        gpt-5.1 (発見)         |  gemini-3-pro-preview (発明)  |       gpt-5.1        |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |   claude-opus-4-5 (異なる)    |  gemini-3-pro-preview (同じ)  |   claude-opus-4-5    |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |    claude-opus-4-5 (同じ)     | gemini-3-pro-preview (異なる) |   claude-opus-4-5    |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） | gemini-3-pro-preview (異なる) |        gpt-5.1 (同じ)         |       gpt-5.1        |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |  gemini-3-pro-preview (同じ)  |   claude-opus-4-5 (異なる)    | gemini-3-pro-preview |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |   claude-opus-4-5 (異なる)    |        gpt-5.1 (同じ)         |       gpt-5.1        |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |        gpt-5.1 (同じ)         |   claude-opus-4-5 (異なる)    |       gpt-5.1        |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） | gemini-3-pro-preview (異なる) |    claude-opus-4-5 (同じ)     | gemini-3-pro-preview |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |  gemini-3-pro-preview (同じ)  |       gpt-5.1 (異なる)        |       gpt-5.1        |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |       gpt-5.1 (異なる)        |    claude-opus-4-5 (同じ)     |       gpt-5.1        |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |    claude-opus-4-5 (同じ)     |       gpt-5.1 (異なる)        |   claude-opus-4-5    |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |        gpt-5.1 (同じ)         | gemini-3-pro-preview (異なる) |       gpt-5.1        |
| 「テセウスの船」（部品が全て入れ替わった船は元の船と同じか？） |       gpt-5.1 (異なる)        |  gemini-3-pro-preview (同じ)  |       gpt-5.1        |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |    claude-opus-4-5 (真実)     |        gpt-5.1 (幸福)         |       gpt-5.1        |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |  gemini-3-pro-preview (幸福)  |        gpt-5.1 (真実)         |       gpt-5.1        |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |        gpt-5.1 (幸福)         |    claude-opus-4-5 (真実)     |       gpt-5.1        |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |    claude-opus-4-5 (幸福)     |        gpt-5.1 (真実)         |       gpt-5.1        |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |  gemini-3-pro-preview (真実)  |        gpt-5.1 (幸福)         |       gpt-5.1        |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |    claude-opus-4-5 (真実)     |  gemini-3-pro-preview (幸福)  |   claude-opus-4-5    |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |  gemini-3-pro-preview (真実)  |    claude-opus-4-5 (幸福)     |   claude-opus-4-5    |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |        gpt-5.1 (幸福)         |  gemini-3-pro-preview (真実)  | gemini-3-pro-preview |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |  gemini-3-pro-preview (幸福)  |    claude-opus-4-5 (真実)     |   claude-opus-4-5    |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |        gpt-5.1 (真実)         |    claude-opus-4-5 (幸福)     |       gpt-5.1        |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |    claude-opus-4-5 (幸福)     |  gemini-3-pro-preview (真実)  | gemini-3-pro-preview |
|      辛い現実か、心地よい仮想現実か、どちらを選ぶべきか？      |        gpt-5.1 (真実)         |  gemini-3-pro-preview (幸福)  |       gpt-5.1        |

</details>

[各レスバの記録](./outputs)

### 勝率

|        モデル        | claude-opus-4-5 | gemini-3-pro-preview | gpt-5.1 | 合計  |
| :------------------: | :-------------: | :------------------: | :-----: | :---: |
|   claude-opus-4-5    |                 |        75.0%         |  18.8%  | 46.9% |
| gemini-3-pro-preview |      25.0%      |                      |  12.5%  | 18.8% |
|       gpt-5.1        |      81.2%      |        87.5%         |         | 84.4% |

## 実行

```
uv run python main.py
```
