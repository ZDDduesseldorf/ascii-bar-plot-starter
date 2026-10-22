import csv


def load_rows(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [
            (row["type"], float(row["value1"]), float(row["value2"])) for row in reader
        ]
