from rich.console import Console


def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)


def render_bar_chart(values, width=40):
    console = Console()
    colors = ["cyan", "green", "yellow", "magenta"]

    if not values:
        return

    maximum = max(value for _, value in values)

    for index, (category, value) in enumerate(values):
        bar = "█" * scale_bar(value, maximum, width)
        color = colors[index % len(colors)]

        console.print(f"{category} | [{color}]{bar:<{width}}[/{color}] {value:.2f}")


if __name__ == "__main__":
    values = [
        ("A", 2.16),
        ("B", 4.33),
        ("C", 6.57),
        ("D", 8.71),
    ]
    render_bar_chart(values)
