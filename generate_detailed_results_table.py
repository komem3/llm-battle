
import csv

def generate_detailed_table():
    try:
        with open("result.csv", mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            # Define headers
            headers = ["テーマ", "サイド1", "サイド2", "勝者"]
            
            # Print Markdown header
            print("| " + " | ".join(headers) + " |")
            print("|" + " :----: |" * len(headers))

            for row in reader:
                theme = row["theme"]
                
                # Format Side 1 and Side 2 as "ModelName (Stance)"
                side1_text = f"{row['player1']} ({row['side1']})"
                side2_text = f"{row['player2']} ({row['side2']})"
                
                # Determine winner name
                winner_idx = int(row["winner"])
                if winner_idx == 0:
                    winner_name = row["player1"]
                else:
                    winner_name = row["player2"]

                # Construct row data
                row_data = [theme, side1_text, side2_text, winner_name]
                
                print("| " + " | ".join(row_data) + " |")

    except FileNotFoundError:
        print("Error: result.csv not found. Please run main.py first to generate it.")
        return

if __name__ == "__main__":
    generate_detailed_table()
