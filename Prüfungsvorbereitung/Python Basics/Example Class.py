# Eine Beispiel Klasse
from abc import ABC, abstractmethod


class Fahrzeug:
    def __init__(self, marke):
        self.marke = marke  # Attribut

    def starten(self):
        print(f"{self.marke} startet.")


# Ein Objekt dieser Klasse erstellen
auto = Fahrzeug("BMW")
auto.starten()  # Ausgabe: BMW startet.


###############################################################################


# Vererbung der Klasse (Inheritance)
class Fahrrad(Fahrzeug):  # Erbt von Fahrzeug
    def klingeln(self):
        print(f"{self.marke} klingelt!")


# Ein Objekt der Klasse mit Methoden der Fahrzeugklasse
bike = Fahrrad("Cube")
bike.starten()    # geerbte Methode
bike.klingeln()   # eigene Methode


###############################################################################


# Polymorphismus (gleiche Methode, unterschiedliches Verhalten je nach Objekt)
class Auto(Fahrzeug):
    def starten(self):
        print(f"{self.marke} (Auto) brummt los!")


class Flugzeug(Fahrzeug):
    def starten(self):
        print(f"{self.marke} (Flugzeug) hebt ab!")


fahrzeuge = [Auto("Audi"), Flugzeug("Boeing"), Fahrrad("KTM")]

for f in fahrzeuge:
    f.starten()  # jede Klasse nutzt ihre eigene Version von .starten()


###############################################################################


# Abstrakte Klasse
class Fahrzeug(ABC):  # abstrakte Basisklasse

    def __init__(self, marke):
        self.marke = marke

    @abstractmethod
    def starten(self):
        pass  # keine konkrete Umsetzung - nur Definition


# Unterklasse mit Umsetzung
class Auto(Fahrzeug):
    def starten(self):
        print(f"{self.marke} startet den Motor.")


class Fahrrad(Fahrzeug):
    def starten(self):
        print(f"{self.marke} beginnt zu rollen.")

# Die Abstrakte Klasse gibt vor die Unterklasse implementiert
