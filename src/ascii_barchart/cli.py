from .analysis import average_value1_by_type
from .chart import render_bar_chart
from .io import load_rows


if __name__ == "__main__":
    rows = load_rows("data/points.csv")
    averages = average_value1_by_type(rows)
    render_bar_chart(averages)