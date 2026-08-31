# Der Abstieg

Ein rundenbasiertes Roguelike im Browser. Fünf Tiefen, dein Fackelöl bestimmt,
wie weit du siehst — und ganz unten wartet Der Namenlose.


## Steuerung

| Taste | Wirkung |
|---|---|
| Pfeiltasten, WASD, hjkl/yubn, Ziffernblock | gehen; gegen einen Gegner laufen greift an |
| Klick auf ein Feld | dorthin laufen · Klick auf einen Gegner: hinlaufen und angreifen |
| `F` | Fähigkeit deiner Klasse |
| `Leertaste` / `.` | eine Runde warten |
| `R` | rasten — heilt 1 Leben je 1 Öl |
| `G` | aufheben |
| `I` / `E` | Beutel: benutzen, anlegen, wegwerfen (Umschalt + Buchstabe wirft direkt weg) |
| `Q` | Aufträge |
| `C` | Heldenbogen |
| `X` | umsehen |
| `V` | Nachrichtenprotokoll |
| `>` (Umschalt + `.`) | Treppe hinabsteigen |
| `M` | Ton an oder aus |
| `L` | Lager (vom Titelbild) |
| `?` / `F1` | Hilfe |
| `Esc` | abbrechen · Pause · speichern |

## Was drinsteckt

**Fünf Tiefen, jede anders gebaut.** Der Kerker aus Quadermauerwerk mit
Türschwellen und Säulenhallen. Die Pilzhöhle als gewachsener Fels aus einem
zellulären Automaten — keine gerade Wand, keine Räume. Die Schmelze mit weiten
Hallen, breiten Werkswegen und Lavarinnen, die selbst leuchten. Die Kammer des
Namenlosen als gebauter Ort mit Säulenkranz und Ritualkreis. Und darunter der
Schlund, endlos und mit wechselnden Bauarten.

**Fackelöl als Uhr.** Es brennt beim Gehen und beim Rasten, und dein Sichtfeld
hängt daran. Geht es aus, siehst du kaum noch einen Schritt weit. Nachschub
kommt aus Fläschchen und aus Fackelschalen, die jede einmal etwas abgeben.

**Drei Klassen** mit eigenen Werten und je einer Fähigkeit: Schildstoß,
Ausweichrolle, Funke.

**Verzauberte Beute.** Zehn Affixe, teils reine Zugewinne, teils Handel.
Adjektive werden nach Geschlecht gebeugt — *gehärteter* Dolch, *gehärtete*
Kriegsaxt, *gehärtetes* Kettenhemd.

**Aufträge** pro Etage mit sichtbarem Lohn, **vier namentliche Zwischenbosse**
mit eigenen Fähigkeiten, **Monster-Affixe** (vernarbt, gepanzert, rasend,
verseucht, flink, brennend).

**Asche als Meta-Fortschritt.** Jeder Lauf zahlt ein, auch der gescheiterte.
Im Lager wird daraus dauerhaft mehr Leben, Angriff, Schutz, Öl, Vorrat — oder
ein Zweiter Atem, der einmal je Abstieg den Todesstoß abfängt.

**Klang.** 28 Geräusche, alle zur Laufzeit über WebAudio erzeugt. Keine Dateien.

## Dateien


Am Spiel wird in `abstieg.html` gearbeitet. Danach:

```
python build.py
```

Das ergänzt Dokumentgerüst, Viewport-Meta, Favicon und Vorschaudaten und
schreibt `index.html`. So driften die beiden Fassungen nicht auseinander.

## Hosting

`index.html` ins Wurzelverzeichnis eines beliebigen Static-Hosts legen. Es gibt
kein Backend, alles läuft im Browser.

Für **GitHub Pages**: in den Repo-Einstellungen unter *Pages* als Quelle den
Branch `main` und den Ordner `/ (root)` wählen. Die Seite liegt dann unter
`https://<benutzer>.github.io/<repo>/`.

## Zwei Hinweise

**Spielstände hängen an der Domain.** Speicherstand und Asche liegen im
`localStorage` des Browsers, und der ist pro Herkunft getrennt. Ein Umzug auf
eine andere Adresse lässt den Fortschritt zurück.

**Auf dem Handy noch nicht spielbar.** Die Seite bricht nicht und scrollt nicht
quer, aber bei 375 px wird eine Kachel nur etwa 11 Pixel groß, und für
Aufheben, Beutel, Rasten und Fähigkeit gibt es keine Knöpfe — nur Tastatur.
