# LLM Battle

LLM 同士をレスバさせて勝敗を決めることで、LLMの性能を比較してみた。

## 結果

### 詳細

- [結果詳細csv](./outputs/result.csv)
- [各レスバの記録](./outputs)

### 勝率

|        モデル        | gemini-3-pro-preview | claude-sonnet-4-5 | gpt-5.1 | 合計 |
| :------------------: | :------------------: | :---------------: | :-----: | :--: |
| gemini-3-pro-preview |                      |       68.8%       |  25.0%  | 31%  |
|  claude-sonnet-4-5   |        31.3%         |                   |  31.3%  | 21%  |
|       gpt-5.1        |        75.0%         |       68.8%       |         | 48%  |

## 実行

```
uv run python main.py
```
