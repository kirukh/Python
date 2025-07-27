# Exception Handling in Python
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Fehler: Division durch Null ist nicht erlaubt."
    except TypeError:
        return "Fehler: Ungültige Eingabetypen. Bitte geben Sie Zahlen ein."
    else:
        return f"Das Ergebnis ist: {result}"
    finally:
        print("Berechnung abgeschlossen.")


# Lernen wie man diese Funktion verwendet
