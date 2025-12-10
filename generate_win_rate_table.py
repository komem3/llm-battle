import csv
from collections import defaultdict


def generate_table():
    win_counts = defaultdict(lambda: defaultdict(int))
    match_counts = defaultdict(lambda: defaultdict(int))
    total_wins = defaultdict(int)
    total_matches = defaultdict(int)
    models = set()

    try:
        with open("result.csv", mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                p1 = row["player1"]
                p2 = row["player2"]
                winner_idx = int(row["winner"])  # 0 for p1, 1 for p2

                models.add(p1)
                models.add(p2)

                # Determine winner and loser names
                if winner_idx == 0:
                    winner_name = p1
                    loser_name = p2
                else:
                    winner_name = p2
                    loser_name = p1

                # Update stats
                win_counts[winner_name][loser_name] += 1
                match_counts[winner_name][loser_name] += 1
                match_counts[loser_name][winner_name] += 1

                total_wins[winner_name] += 1
                total_matches[winner_name] += 1
                total_matches[loser_name] += 1

    except FileNotFoundError:
        print("Error: result.csv not found. Please run main.py first.")
        return

    sorted_models = sorted(list(models))

    # --- Generate Markdown Table ---
    header = "| モデル | " + " | ".join(sorted_models) + " | 合計 |"
    print(header)
    print("| :-------: |" + " :-------: |" * len(sorted_models) + " :-------: |")

    for model_row in sorted_models:
        row_data = [model_row]

        for model_col in sorted_models:
            if model_row == model_col:
                row_data.append("")  # Diagonal is empty
            else:
                wins = win_counts[model_row][model_col]
                matches = match_counts[model_row][model_col]

                if matches > 0:
                    win_rate = (wins / matches) * 100
                    row_data.append(f"{win_rate:.1f}%")
                else:
                    row_data.append("-")

        # Calculate overall win rate for the model
        t_wins = total_wins[model_row]
        t_matches = total_matches[model_row]

        if t_matches > 0:
            overall_win_rate = (t_wins / t_matches) * 100
            row_data.append(f"{overall_win_rate:.1f}%")
        else:
            row_data.append("-")

        print("| " + " | ".join(row_data) + " |")


if __name__ == "__main__":
    generate_table()
