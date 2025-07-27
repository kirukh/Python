# Einfach Suche
import re

text = "Ich liebe Python!"
muster = "Python"

resultat = re.search(muster, text)
if resultat:
    print("Gefunden:", resultat.group())


# Alle Zahlen aus einem Text extrahieren
text = "Heute ist der 27.07.2025 und es ist 30 Grad."
zahlen = re.findall(r'\d+', text)
print(zahlen)  # ['27', '07', '2025', '30']


# Email-Adresse finden
text = "Meine Emails sind max@test.de und info@domain.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)  # ['max@test.de', 'info@domain.org']


# Ersetzten von Wörtern
text = "Python ist toll, Python ist schnell."
neu = re.sub(r'Python', 'JavaScript', text)
print(neu)  # JavaScript ist toll, JavaScript ist schnell.

# Aufteilen eines Textes
text = "Name: Max; Alter: 28; Ort: Berlin"
teile = re.split(r';\s*', text)
print(teile)  # ['Name: Max', 'Alter: 28', 'Ort: Berlin']
