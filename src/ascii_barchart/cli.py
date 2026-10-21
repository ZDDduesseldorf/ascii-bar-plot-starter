import os
import sys

from .analysis import average_value1_by_type
from .chart import render_bar_chart
from .io import load_rows


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m ascii_barchart.cli <csv-file>")
        raise SystemExit(1)

    csv_path = os.path.abspath(sys.argv[1])

    if not os.path.isfile(csv_path):
        print(f"File not found: {csv_path}")
        raise SystemExit(1)

    rows = load_rows(csv_path)
    averages = average_value1_by_type(rows)
    print(averages)
    render_bar_chart(averages)


if __name__ == "__main__":
    main()