# Import-Reihenfolge: Standardbibliothek, Drittanbieter, lokale Module
import os
import sys

import numpy as np

# import mein_modul


# Einrückung (Indentation)
def begrüßung(name):
    if name:
        print("Hallo", name)


# Benennung von Variablen und Funktionen
max_wert = 100  # Kleinbuchstaben und Unterstriche für Variablen


# Kleinbuchstaben und Unterstriche für Funktionen
def berechne_summe(a, b):
    return a + b


class MeinAuto:  # CamelCase für Klassen
    pass


# Leerzeilen (Whitespace)
def foo():
    pass


def bar():
    pass


# Kommentare
def addiere(a, b):
    """Gibt die Summe von a und b zurück."""  # Docstring für Funktionen und Klassen
    return a + b


# Maximale Zeilenlänge
# PEP 8 empfiehlt eine maximale Zeilenlänge von 79 Zeichen.
text = ("Dies ist ein sehr langer Text, "
        "der über mehrere Zeilen geschrieben wird.")
