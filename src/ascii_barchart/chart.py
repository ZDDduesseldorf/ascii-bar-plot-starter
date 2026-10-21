from rich.console import Console
from rich.text import Text

STYLES = {
    "A": "bold cyan",
    "B": "bold magenta",
    "C": "bold red",
    "D": "bold green",
}

# standalone test
# values = [
#     ("A", 2.16),
#     ("B", 4.33),
#     ("C", 6.57),
#     ("D", 8.71),
# ]

def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)

def render_bar_chart(values):
    max_val = max(val for _, val in values)

    for label, val in values:

        console = Console()
        
        length = scale_bar(val, max_val, width=20)
        line = Text(f"{label} | ")
        line.append("█" * length, style=STYLES[label])
        line.append(f" {val}")

        console.print(line)

render_bar_chart(values)






