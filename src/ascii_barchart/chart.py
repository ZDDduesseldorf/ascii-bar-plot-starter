from rich.console import Console

values = [
    ("A", 2.16),
    ("B", 4.33),
    ("C", 6.57),
    ("D", 8.71),
]
def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)

def render_bar_chart(values):
    console = Console()
    maximum = max(value for _, value in values)
    for label, value in values:
        bar = "█" * scale_bar(value, maximum)
        console.print(f"{label} [green]{bar}[/green] {value}")
        
if __name__ == "__main__":
    render_bar_chart(values)
