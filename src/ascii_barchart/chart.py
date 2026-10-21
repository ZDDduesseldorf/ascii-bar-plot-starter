from rich import print
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
    print("[bold yellow]So verteilen sich die verschiedenen Kategorien:")
    width = 50
    max_value = 0
    for e in values:
        if e[1] > max_value:
            max_value = e[1]
    max_chart = math.ceil(max_value)

    for e in values:
        scale = scale_bar(e[1], max_chart, width)
        empty = scale - width
        print(e[0], scale * "-", (width - scale) * " ", e[1])

    return

render_bar_chart(values)