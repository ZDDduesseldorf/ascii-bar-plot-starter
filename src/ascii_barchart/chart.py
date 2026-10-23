from rich.console import Console

# Beispieldaten zum Testen des Balkendiagramms
values = [
    ("A", 2.16),
    ("B", 4.33),
    ("C", 6.57),
    ("D", 8.71),
]

# Berechnet die Länge eines Balkens anhand des größten Wertes
def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    # Skaliert den Wert auf die gewünschte Breite
    return round(value / maximum * width)

# Erstellt ein farbiges horizontales Balkendiagramm
def render_bar_chart(values, width=40):
    
    # Console ermöglicht farbige Ausgaben im Terminal
    console = Console()

    # Ermittelt den größten Wert für die Skalierung
    maximum = max(value for name, value in values)

    # Vier Farben für die Balken
    colors = ["red", "green", "blue", "yellow"]

    # Durchläuft alle Kategorien und ihre Werte
    for i, (name,value) in enumerate(values):
        
        # Berechnet die Balkenlänge
        length = scale_bar(value, maximum, width)
        
        # Erstellt den Balken mit Blockzeichen
        bar = "█" * length
        
        # Gibt den Balken mit Farbe und Wert aus
        console.print(f"{name}: {bar} {value:.2f}", style=colors[i])

# Startet das Diagramm beim direkten Ausführen der Datei
if __name__ == "__main__":
    render_bar_chart(values)