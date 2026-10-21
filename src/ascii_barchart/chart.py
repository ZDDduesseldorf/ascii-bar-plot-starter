from rich.console import Console
import math

values = [
    ("A", 2.16),
    ("B", 4.33),
    ("C", 6.57),
    ("D", 8.71),
]

def scale_bar(value, maximum, width):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)


def render_bar_chart(values):
    console = Console()
    console.print("[bold yellow]So verteilen sich die verschiedenen Kategorien:[/bold yellow]")
    width = 50
    max_value = 0
    for e in values:
        if e[1] > max_value:
            max_value = e[1]
    max_chart = math.ceil(max_value)
    i = 0
    colors = ["dark_turquoise", "purple4", "medium_orchid3", "gold3"]
    for i, (name, value) in enumerate(values):
        scale = scale_bar(value, max_chart, width)
        bar = "-" * scale
        
        console.print(name, scale * "-", (width - scale) * " ", value, style = colors[i])
        

    return



render_bar_chart(values)