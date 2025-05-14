# Nim AI mit Q-Learning

Dieses Projekt implementiert eine Künstliche Intelligenz (KI), die mithilfe von Q-Learning das klassische Spiel **Nim** erlernt und gegen menschliche Spieler antreten kann.

## 🧠 Ziel des Projekts

Das Ziel ist es, eine KI zu programmieren, die selbstständig durch Training lernt, optimale Züge zu machen, um das Spiel **Nim** zu gewinnen. Anschließend kannst du gegen die KI in einer grafischen Benutzeroberfläche (GUI mit Pygame) antreten.

## 🔗 Repository-Struktur

```
Nim-AI-Template/
│
├── nim.py          # Spiellogik & Q-Learning KI (Hauptimplementierung)
├── play.py         # Einstiegspunkt: Training & Spielstart
├── game.py         # Grafische Oberfläche (Pygame)
├── test.py         # Tests für die KI-Funktionen
└── README.md       # Dieses Dokument
```

## 📦 Installation & Start

```bash
# Repository klonen
git clone https://github.com/patkordum/Nim-AI-template.git
cd Nim-AI-template

# Spiel starten (trainiert zuerst die KI und öffnet GUI)
python play.py
```

## 🔍 Funktionsweise der KI

Die KI nutzt **Q-Learning**, ein Verfahren des Reinforcement Learning. Dabei wird jeder mögliche Spielzustand und jede mögliche Aktion mit einem **Q-Wert** bewertet, der die Qualität dieser Aktion in dem Zustand beschreibt.

### Zustand (State)

Ein Zustand ist die aktuelle Verteilung der Steine in den Haufen, z. B.:

```python
[1, 1, 3, 5]
```

### Aktion (Action)

Eine Aktion ist ein Tupel `(i, j)`, das bedeutet: „Entferne **j** Steine aus Haufen **i**“.
Beispiel:

```python
(3, 2)  # Entferne 2 Steine aus Haufen 3
```

### Q-Wert-Tabelle (`self.q`)

Diese speichert die Bewertung jeder (Zustand, Aktion)-Kombination.

```python
self.q[((1, 1, 3, 5), (3, 2))] = 0.75
```

### Q-Learning-Formel

Die Bewertung erfolgt durch:

```python
Q(s, a) ← old_q + alpha * (reward + future_q - old_q)
```

## 🔧 Wichtige Methoden (nim.py)

### `get_q_value(state, action)`

Gibt den Q-Wert eines bestimmten Zustands und einer Aktion zurück (0, falls unbekannt).

### `update_q_value(state, action, old_q, reward, future_q)`

Aktualisiert den Q-Wert nach dem Q-Learning-Update-Regel.

### `best_future_reward(state)`

Gibt den höchsten bekannten Q-Wert für mögliche Folgeaktionen zurück.

### `choose_action(state, epsilon=True)`

Wählt eine Aktion gemäß einer ε-greedy-Strategie:

* Mit Wahrscheinlichkeit ε: zufällige Aktion (Exploration)
* Mit Wahrscheinlichkeit 1 – ε: beste bekannte Aktion (Exploitation)

## 🧪 Testen (test.py)

Die Datei `test.py` enthält vorbereitete Tests für alle wichtigen Methoden. Du kannst sie starten mit:

```bash
python test.py
```

## 🎮 Spielverlauf (game.py)

* GUI mit Pygame
* Du kannst mit der Maus Steine auswählen und entfernen
* Nach deinem Zug ist die KI dran

## 🏁 Trainingsstart (play.py)

Startet automatisch ein Training mit 1000 Partien und beginnt dann das Spiel:

```python
ai = train(1000)
start_game(ai)
```

## 📈 Weiterentwicklung

* Q-Werte speichern und wiederverwenden
* Spielmodi: Mensch gegen Mensch, KI gegen KI
* Anpassbare Anzahl an Haufen/Steinen
* MCTS oder Deep Q-Learning ergänzen

## 📚 Quellen & Tools

* Python 3
* Pygame
* Reinforcement Learning Prinzipien (Q-Learning)

---

Viel Spaß beim Ausprobieren – und schlag die KI, wenn du kannst! 🤖
