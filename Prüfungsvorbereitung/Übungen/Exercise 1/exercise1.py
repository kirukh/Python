import json

with open("Übungen/Exercise 1/example.json", "r") as file:
    data = json.load(file)

print(data)  # Ausgabe des geladenen JSON-Inhalts

with open("Übungen/Exercise 1/example.json", "w") as file:
    # Beispiel für das Hinzufügen eines neuen Schlüssels
    data["NEW_KEY"] = "New Value"
    json.dump(data, file, indent=4)

with open("Übungen/Exercise 1/anotherexample.json", "a") as file:
    json.dump(data, file, indent=4)  # Anhängen der Daten an eine andere Datei
