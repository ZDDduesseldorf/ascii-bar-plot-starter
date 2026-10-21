# Praktikum: Vom CSV-Datensatz zum sauberen Python-Projekt

## Horizontales ASCII-Balkendiagramm mit `rich`

**Teamgröße:** 2 Personen  
**Werkzeuge:** VS Code, Git/GitHub, `uv`, Python, `rich`  
**Schwerpunkt:** Environment, Dependencies, `pyproject.toml`, `.gitignore`, `src`-Layout, Packages/Module, relative Imports und Team-Workflow

> **Wichtig:** Das Balkendiagramm ist bewusst einfach. Die eigentliche Aufgabe lautet nicht „Programmiert einen tollen Plot“, sondern: **Macht aus einer kleinen Idee ein sauberes, reproduzierbares Python-Projekt.**

---

# Szenario

Ihr bekommt ein Starter-Repository mit einem Datensatz:

```csv
type,value1,value2
A,1.2,7.8
B,2.7,5.1
C,4.8,8.4
D,8.2,2.0
...
```

Für jeden Typ `A`, `B`, `C`, `D` soll der Mittelwert von `value1` berechnet und als **horizontales Balkendiagramm direkt im Terminal** ausgegeben werden.

Ungefähr so:

```text
Average value1 by type

A | ██████████                               2.16
B | ████████████████████                     4.33
C | ██████████████████████████████           6.57
D | ████████████████████████████████████████ 8.71
```

Die Balken sollen mit `rich` je nach Typ unterschiedlich eingefärbt werden. `value2` wird in dieser Variante noch nicht visualisiert – die Spalte bleibt absichtlich im Datensatz, damit euer Loader mit realistischeren Daten umgehen muss.

---

# Was heute gelernt werden soll

Am Ende sollt ihr erklären können:

- Warum jedes Projekt ein eigenes Environment haben sollte.
- Was `.venv` enthält und warum es **nicht** ins Repository gehört.
- Welche Rolle `pyproject.toml` spielt.
- Warum `uv.lock` committed wird.
- Was `src/ascii_barchart/` zu einem Python-Package macht.
- Warum `__init__.py` vorhanden ist.
- Wie Module innerhalb eines Packages voneinander importieren.
- Warum wir das Programm mit `python -m ...` starten.
- Wie zwei Personen über Branches, Push/Pull und Pull Requests zusammenarbeiten.

Die automatische GitHub Action prüft viele dieser Punkte. **CI selbst ist heute noch nicht das Thema** – betrachtet sie einfach als automatisches Feedback.

---

# Starter-Repository

Zu Beginn enthält das Repository ungefähr:

```text
ascii-bar-project-starter/
├── .ci/
│   └── check_project.py
├── .github/
│   └── workflows/
│       └── project-check.yml
├── data/
│   └── points.csv
├── resources/
│   ├── HINTS.md
│   └── VSCode_Git_Workflow.md
└── README.md
```

Noch **nicht** vorhanden sind unter anderem:

```text
.gitignore
pyproject.toml
uv.lock
src/
```

Die Dateien unter `.ci/` und `.github/` werden nicht verändert.

---

# Zielstruktur

```text
ascii-bar-project/
├── .ci/
├── .github/
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
├── data/
│   └── points.csv
└── src/
    └── ascii_barchart/
        ├── __init__.py
        ├── io.py
        ├── analysis.py
        ├── chart.py
        └── cli.py
```

Je nach `uv`-Version können zusätzlich `.python-version` und `py.typed` entstehen. Das ist in Ordnung.

---

# Git-Regel für dieses Praktikum

Ihr arbeitet **zu zweit an einem gemeinsamen Remote-Repository**.

Beide Personen müssen:

- das Repository selbst lokal in VS Code klonen,
- mindestens einen eigenen Branch erstellen,
- eigene Python-Code-Commits erzeugen,
- den eigenen Branch pushen,
- mindestens einmal Änderungen vom Remote holen,
- mindestens einen Pull Request erstellen oder reviewen.

Am Ende müssen im Git-Verlauf **Beiträge von beiden Personen** sichtbar sein.

---

# Teil A – Team-Repository in VS Code öffnen

## 0. Auf EIN gemeinsames Remote Repository einigen!

Ihr arbeitet zu zweit, benötigt aber ein gemeinsames Remote-Repository, auf das beide schreiben können.

**Person A**  
1. Öffnet das bereitgestellte Starter-Repository auf GitHub.
2. Klickt auf Fork und erstellt einen Fork im eigenen GitHub-Account.
3. Öffnet im neuen Fork Settings → Collaborators → Add people.
4. Fügt **Person B** über den GitHub-Benutzernamen als Collaborator hinzu.

**Person B**  
5. Akzeptiert die GitHub-Einladung.

Danach verwenden beide Personen den Fork von Person A als gemeinsames Team-Repository.

Beide öffnen in VS Code:

**Command Palette → Git: Clone**

und klonen dieselbe URL, zum Beispiel:
```bash
https://github.com/alice/ascii-scatter-project-starter.git
```

Danach öffnen beide den geklonten Ordner in VS Code.

Kontrolliert gemeinsam auf GitHub, dass ihr wirklich im selben Fork arbeitet.

Ab jetzt gilt:
```bash
gemeinsamer Fork auf GitHub = Remote-Repository des Teams
eigener Rechner             = eigener lokaler Clone
```

Beide arbeiten lokal in ihrem eigenen Clone. Änderungen werden erst durch Commit + Push zum gemeinsamen GitHub-Repository übertragen. Änderungen der anderen Person erscheinen erst nach Pull im eigenen lokalen Clone.

## 1. Beide Personen arbeiten lokal

Beide Teammitglieder müssen das Repository auf dem **eigenen Rechner** haben.

### In VS Code

1. VS Code öffnen.
2. `Ctrl+Shift+P` (Windows/Linux) bzw. `Cmd+Shift+P` (macOS).
3. **Git: Clone** auswählen.
4. URL eures gemeinsamen Team-Repositories einfügen.
5. Einen lokalen Ordner auswählen.
6. Nach dem Clone **Open** / **Open Repository** wählen.
7. Unten links kontrollieren, dass ihr auf Branch `main` seid.

Öffnet anschließend das integrierte Terminal über **Terminal → New Terminal**.

Kurzer Kontrollbefehl:

```bash
git status
```

> **Terminal-Hinweis:** Das Klonen ginge auch mit `git clone <URL>`. Ab jetzt arbeiten wir aber primär über VS Code Source Control.

---

# Teil B – Python-Projekt aufsetzen

## 2. Setup-Branch anlegen

**Person A** übernimmt zunächst den Setup-Branch.

### VS Code

1. Unten links auf `main` klicken.
2. **Create new branch...** wählen.
3. Branch nennen: `setup/python-project`.

Alternativ über Command Palette: **Git: Create Branch**.

> Terminal-Hinweis: `git switch -c setup/python-project`

## 3. uv-Projekt initialisieren

Im VS-Code-Terminal:

```bash
uv init --lib --name ascii-barchart
uv venv
uv add rich
```

Danach kontrolliert gemeinsam:

- Was wurde neu erzeugt?
- Wo liegt `.venv`?
- Was steht in `pyproject.toml`?
- Was steht ungefähr in `uv.lock`?
- Ist `rich` in `pyproject.toml` eingetragen?

Falls ihr die Python-Extension in VS Code nutzt:

1. `Ctrl/Cmd+Shift+P`
2. **Python: Select Interpreter**
3. Python aus `.venv` wählen

Der folgende Befehl muss funktionieren:

```bash
uv run python -c "import rich; print('rich import works')"
```

## 4. `.gitignore`

Kontrolliert oder erstellt `.gitignore`. Mindestens:

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/
.DS_Store
```

Frage an euch:

> Warum committen wir `uv.lock`, aber nicht `.venv/`?

## 5. Setup über VS Code committen und pushen

Öffnet links **Source Control** (`Ctrl/Cmd+Shift+G`).

1. Unter **Changes** die geänderten Dateien anschauen.
2. `.venv` darf dort **nicht** als zu committen auftauchen.
3. Mit `+` die gewünschten Dateien **stagen** – oder bei **Changes** alle stagen.
4. Oben eine Commit-Nachricht eingeben, z. B. `Set up uv Python project`.
5. **Commit** klicken.
6. **Publish Branch** bzw. **Push** klicken.

> Terminal-Hinweis: Das entspricht ungefähr `git add ...`, `git commit -m ...` und `git push -u origin setup/python-project`.

## 6. Pull Request

Auf GitHub:

1. Repository öffnen.
2. **Compare & pull request** auswählen.
3. PR von `setup/python-project` nach `main` erstellen.
4. **Person B** liest die Änderungen.
5. Person B prüft besonders `pyproject.toml` und `.gitignore`.
6. PR mergen.

Danach wechseln **beide Personen** in VS Code zurück auf `main` und holen die Änderungen:

- unten links Branch → `main`
- Source Control → `...` → **Pull**

oder **Sync Changes**, wenn VS Code dies anbietet.

> Terminal-Hinweis: `git switch main` und `git pull`.

---

# Teil C – Erst Schnittstellen festlegen

Bevor ihr parallel arbeitet, einigt euch auf diese drei Schnittstellen:

```python
load_rows(csv_path)
```

liefert:

```python
[("A", 1.2, 7.8), ("B", 2.7, 5.1), ...]
```

```python
average_value1_by_type(rows)
```

liefert ungefähr:

```python
[("A", 2.16), ("B", 4.33), ("C", 6.57), ("D", 8.71)]
```

und:

```python
render_bar_chart(values, width=40)
```

bekommt diese Mittelwerte und gibt den Plot aus.

> Genau deshalb sind klare Schnittstellen nützlich: Nun könnt ihr an unterschiedlichen Modulen arbeiten, ohne gleichzeitig dieselbe Datei zu bearbeiten.

---

# Teil D – Parallel arbeiten

## 7. Person A: CSV + Auswertung

Branch: `feature/data-analysis`

### VS Code Branch erstellen

- unten links aktuellen Branch anklicken
- **Create new branch...**
- `feature/data-analysis`

Person A erstellt/bearbeitet:

```text
src/ascii_barchart/io.py
src/ascii_barchart/analysis.py
```

Ziel:

```python
rows = load_rows("data/points.csv")
averages = average_value1_by_type(rows)
```

soll ungefähr ergeben:

```text
A 2.16
B 4.33
C 6.57
D 8.71
```

Wenn ihr beim Python-Code hängt, steht in `resources/README_HINTS.md` fast die komplette notwendige Logik.

Anschließend über **Source Control**:

1. Änderungen prüfen.
2. Stagen.
3. Commit z. B. `Add CSV loading and aggregation`.
4. **Publish Branch / Push**.
5. Pull Request auf GitHub öffnen.

## 8. Person B: Rich-Balkendiagramm

Branch: `feature/bar-chart`

Person B arbeitet an:

```text
src/ascii_barchart/chart.py
```

Zum Entwickeln kann zunächst mit festen Beispieldaten gearbeitet werden:

```python
values = [
    ("A", 2.16),
    ("B", 4.33),
    ("C", 6.57),
    ("D", 8.71),
]
```

Ziel:

```python
render_bar_chart(values)
```

soll vier horizontale, farbige Balken erzeugen.

Hilfreiche Teilfunktion:

```python
def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)
```

Auch Person B:

1. Source Control öffnen.
2. Änderungen stagen.
3. Commit z. B. `Add Rich bar chart renderer`.
4. Branch publishen/pushen.
5. Pull Request öffnen.

**Wichtig:** Zu diesem Zeitpunkt müssen im Repository bereits Python-Code-Commits von **beiden Personen** vorhanden sein.

---

# Teil E – Gegenseitig reviewen und mergen

## 9. Reviews

Jede Person reviewed den Pull Request der anderen Person.

Nicht nur „Looks good“ klicken. Prüft mindestens:

- Ist die Datei im richtigen Package-Ordner?
- Ist die Funktion verständlich benannt?
- Entspricht Rückgabe/Parameter der vereinbarten Schnittstelle?
- Gibt es unnötig duplizierten Code?
- Werden keine lokalen absoluten Pfade verwendet?

Danach beide PRs mergen.

## 10. Lokale Repositories aktualisieren

In VS Code:

1. auf `main` wechseln
2. Source Control → `...` → **Pull** bzw. **Sync Changes**

Nun sollten beide lokalen Repositories die Dateien der anderen Person enthalten.

---

# Teil F – Module verbinden

## 11. `cli.py`

Erstellt gemeinsam:

```text
src/ascii_barchart/cli.py
```

Ihr dürft hierfür den Code aus `resources/README_HINTS.md` nahezu vollständig übernehmen. Entscheidend sind heute die Imports:

```python
from .analysis import average_value1_by_type
from .chart import render_bar_chart
from .io import load_rows
```

Achtet auf den Punkt vor den Modulnamen. Das sind **relative Imports innerhalb desselben Packages**.

Programm vom Repository-Root starten:

```bash
uv run python -m ascii_barchart.cli data/points.csv
```

Nicht empfohlen:

```bash
python src/ascii_barchart/cli.py
```

Warum? Beim direkten Start einer einzelnen Datei fehlt Python der Package-Kontext für die relativen Imports.

## 12. Integrations-Commit über VS Code

Wieder Source Control:

- Änderungen kontrollieren
- stagen
- Commit z. B. `Connect modules in CLI`
- Push

Falls ihr dafür einen neuen Branch verwendet habt: PR erstellen und mergen.

---

# Teil G – Automatisches Feedback

## 13. GitHub Actions ansehen

Auf GitHub:

1. **Actions** öffnen.
2. neuesten Lauf **Project structure check** öffnen.
3. **Run project checker** aufklappen.

Beispiel:

```text
[PASS] pyproject.toml exists
[PASS] uv.lock exists
[PASS] .venv is listed in .gitignore
[PASS] rich is declared as dependency
[PASS] src/ascii_barchart/__init__.py exists
...
[FAIL] commits from at least two contributors
```

Behandelt jede `FAIL`-Zeile wie einen Hinweis eines automatischen Tutors: verstehen → lokal korrigieren → über VS Code committen → pushen → CI erneut anschauen.

---

# Definition of Done

Euer Praktikum ist abgeschlossen, wenn:

- [ ] beide Teammitglieder das Repository selbst lokal in VS Code geklont haben,
- [ ] beide Teammitglieder eigene Python-Code-Commits haben,
- [ ] beide mindestens einen eigenen Branch verwendet haben,
- [ ] Pull Requests und Reviews verwendet wurden,
- [ ] mindestens einmal Änderungen über **Pull** / **Sync** vom Remote geholt wurden,
- [ ] `.venv/` lokal existieren darf, aber nicht von Git getrackt wird,
- [ ] `pyproject.toml` vorhanden ist,
- [ ] `rich` als Dependency eingetragen ist,
- [ ] `uv.lock` committed ist,
- [ ] `src/ascii_barchart/__init__.py` existiert,
- [ ] relative Imports zwischen den Modulen verwendet werden,
- [ ] `uv run python -m ascii_barchart.cli data/points.csv` funktioniert,
- [ ] beide lokalen Clones nach einem finalen Pull auf demselben Stand sind,
- [ ] die GitHub-CI grün ist.

---

# Abschlussfragen

1. Warum sollte ich `.venv/` nicht einfach mit auf GitHub hochladen?
2. Warum reicht es nicht, nur zu sagen „Installiere Rich“?
3. Was ist der Unterschied zwischen `pyproject.toml` und `uv.lock`?
4. Wofür brauchen wir `__init__.py`?
5. Warum beginnen die Imports in `cli.py` mit `.`?
6. Warum können Person A und Person B gleichzeitig arbeiten, ohne dieselbe Datei zu editieren?
7. Was müsste eine dritte Person tun, um morgen einen frischen Clone des Projekts auszuführen?
# fuck asser