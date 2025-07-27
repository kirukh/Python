import yaml

# YAML-Datei einlesen
with open("example.yaml", "r") as f:
    config = yaml.safe_load(f)

# Zugriff auf die Daten
print("App-Name:", config["app"]["name"])
print("Version:", config["app"]["version"])
print("Debug-Modus:", config["app"]["debug"])

print("\nDatenbank-Verbindung:")
print("Host:", config["database"]["host"])
print("Port:", config["database"]["port"])
print("Benutzer:", config["database"]["username"])

print("\nAktivierte Features:")
for feature in config["features"]:
    print("-", feature)

print("\nLogging-Level:", config["logging"]["level"])
print("Log-Datei:", config["logging"]["file"])
