import csv


def load_rows(csv_path):
    rows = []
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        for record in reader:
            rows.append(
                (
                    record["type"],
                    float(record["value1"]),
                    float(record["value2"]),
                )
            )
    return rows