# Normales Textfile Handling
# Datei schreiben
import json
import csv
with open("test.txt", "w") as file:
    file.write("Hallo Welt!\n")
    file.write("Dies ist eine zweite Zeile.")

# Datei lesen
with open("test.txt", "r") as file:
    inhalt = file.read()
    print(inhalt)

# Zeilenweise lesen
with open("test.txt", "r") as file:
    for zeile in file:
        print(zeile.strip())  # .strip() entfernt \n

# Datei anhängen
with open("test.txt", "a") as file:
    file.write("\nNeue Zeile am Ende.")

# Wenn man files ohne with öffnet muss man diese auch wieder schließen
file = open("datei.txt", "r")
inhalt = file.read()
file.close()

# Weiter wichtige Befehle für das File Handling
file.read()  # Ganzen Inhalt lesen
file.readline()  # Eine einzelne Zeile lesen
file.readlines()  # Gibt Liste aller Zeilen zurück
file.write(text)  # Text schreiben
file.writelines([...])  # Mehrere Zeilen auf einmal schreiben


#########################################################################################################


# CSV Datein
# Aufbau
Name, Alter
Anna, 25
Tom, 30

# CSV lesen

with open("personen.csv", "r") as file:
    reader = csv.reader(file)
    for zeile in reader:
        print(zeile)

# Ausgabe dazu
['Name', 'Alter']
['Anna', '25']
['Tom', '30']

# CSV schreiben

# new line ist wichtig, damit keine leeren Zeilen dazwischen entstehen
with open("personen.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Alter"])
    writer.writerow(["Anna", 25])
    writer.writerow(["Tom", 30])


# CSV als dict einlesen

with open("personen.csv", "r") as file:
    reader = csv.DictReader(file)
    for zeile in reader:
        print(zeile["Name"], zeile["Alter"])

# Ein dict zu einer csv Datei schreiben lassen

daten = [
    {"Name": "Anna", "Alter": 25},
    {"Name": "Tom", "Alter": 30}
]

with open("personen.csv", "w", newline="") as file:
    feldnamen = ["Name", "Alter"]
    writer = csv.DictWriter(file, fieldnames=feldnamen)
    writer.writeheader()
    writer.writerows(daten)


#########################################################################################################


# Json Datein
# Aufbau
{
    "name": "Anna",
    "alter": 25
}

# JSON lesen

with open("daten.json", "r") as file:
    daten = json.load(file)
    print(daten["name"])  # Ausgabe: Anna

# JSON schreiben

daten = {
    "name": "Tom",
    "alter": 30
}

with open("daten.json", "w") as file:
    json.dump(daten, file, indent=4)
