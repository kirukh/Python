# Model für Benutzer
class CalculatorModel:
    def add(self, a, b):
        try:
            return float(a) + float(b)
        except ValueError:
            return "Ungültige Eingabe"
