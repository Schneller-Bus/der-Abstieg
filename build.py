"""Baut aus abstieg.html eine eigenstaendige index.html fuer den Webserver.

abstieg.html ist im Artifact-Format geschrieben: ohne <!doctype>, <html>, <head>.
Fuer echtes Hosting fehlen dort Viewport-Meta, Favicon und Vorschaubilder.
Dieses Skript ergaenzt genau das und laesst das Spiel selbst unveraendert.

Aufruf:  python build.py
"""

import io
import os
import re

HIER = os.path.dirname(os.path.abspath(__file__))
QUELLE = os.path.join(HIER, "abstieg.html")
ZIEL = os.path.join(HIER, "index.html")

TITEL = "Der Abstieg"
BESCHREIBUNG = (
    "Ein rundenbasiertes Roguelike in fünf Tiefen. Dein Fackelöl bestimmt, "
    "wie weit du siehst — und ganz unten wartet Der Namenlose."
)

# Fackel als Inline-SVG, damit kein zweiter Dateiabruf noetig ist.
FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' rx='12' fill='%2314110E'/%3E"
    "%3Cpath d='M32 8c6 9 12 13 12 22a12 12 0 0 1-24 0c0-5 3-8 6-12 1 4 3 6 6 7"
    "-2-6 0-12 0-17z' fill='%23E8A94B'/%3E"
    "%3Cpath d='M32 26c3 4 5 6 5 10a5 5 0 0 1-10 0c0-3 2-5 5-10z' fill='%23FFF0C4'/%3E"
    "%3Crect x='29' y='44' width='6' height='14' rx='2' fill='%236B5335'/%3E"
    "%3C/svg%3E"
)


def baue():
    quelltext = io.open(QUELLE, encoding="utf-8").read()

    # Kopfteil (Schriften + Stil) vom Rumpf trennen.
    ende_stil = quelltext.index("</style>") + len("</style>")
    kopf_roh = quelltext[:ende_stil]
    rumpf = quelltext[ende_stil:].lstrip("\n")

    # charset und title stellt das Geruest selbst - im Kopfteil doppeln sie sonst.
    kopf = re.sub(r'^\s*<meta charset="utf-8">\s*\n', "", kopf_roh)
    kopf = re.sub(r"^\s*<title>.*?</title>\s*\n", "", kopf, flags=re.S)
    kopf = kopf.strip()

    dokument = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{TITEL}</title>
<meta name="description" content="{BESCHREIBUNG}">
<meta name="theme-color" content="#14110E">
<meta name="color-scheme" content="dark">
<link rel="icon" href="{FAVICON}">
<link rel="apple-touch-icon" href="{FAVICON}">

<meta property="og:type" content="website">
<meta property="og:title" content="{TITEL}">
<meta property="og:description" content="{BESCHREIBUNG}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{TITEL}">
<meta name="twitter:description" content="{BESCHREIBUNG}">

{kopf}
</head>
<body>
{rumpf}
</body>
</html>
"""

    io.open(ZIEL, "w", encoding="utf-8", newline="\n").write(dokument)
    groesse = os.path.getsize(ZIEL)
    print("geschrieben: %s (%.1f KB)" % (ZIEL, groesse / 1024.0))
    return dokument


if __name__ == "__main__":
    baue()
