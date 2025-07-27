import control
import questionary
from prettytable import PrettyTable

#Funktion zum Ausgeben der Ergebnisse im CLI
def print_output_table(content):
	#Löscht Terminal Inhalt und setzt Cursorposition auf 0,0
	print("\033[0m\033[2J\033[H\033[0m")
	table = PrettyTable()
	table.field_names = ["Artikel Überschrift"]
	#Falls Ergebnisse gefunden wurden werden diese ausgegeben. Ansonsten wird "Keine Ergebnisse gefunden!" ausgegeben 
	if content:
		for element in content:
			table.add_row([element])
	else:
		table.add_row(["Keine Ergebnisse gefunden!"])
	print(table)

#holt sich die Websites aus config.json. control -> model	
websites = control.get_websites()
#gibt die Fragen aus
answers = questionary.form(first = questionary.select("Von welcher Webseite soll gescraped werden: ", choices = [i for i in websites.keys()]), second = questionary.text("Nach welchen wörtern möchtet du filtern: "), third = questionary.text("Bitte gib einen Dateinamen zum Speichern der Ergebniss ein: ")).ask()

#Je nach gewählter website wird die entsprechende Funktion aufgerufen
titles = []
if answers["first"] == "National Geographic":
	titles = control.connect_to_national_geographic()
elif answers["first"] == "Spektrum":
	titles = control.connect_to_spektrum()
elif answers["first"] == "Tagesschau":
	titles = control.connect_to_tagesschau()
elif answers["first"] == "Forschung und Wissen":
	titles = control.connect_to_forschung_und_wissen()

if titles:
	#verwandle liste in set und danach wieder in liste, um duplikate zu löschen
	titles = list(set([title.lower().strip() for title in titles]))
	#hier werden die Ergebnisse entsprechend der Usereingabe gefiltert
	filtered = []
	filtered = control.filter_titles(titles, answers["second"])
	print_output_table(filtered)
	if answers["third"]:
		control.save_output(filtered, answers["third"])
	else:
		#falls kein Dateiname angegeben wurde
		print("\033[31;1;4m" + "keine datei zum Speichern ausgewählt" + "\033[0m")
			
else:
	#falls keine Ergebnisse gefunden wurden
	print("\033[31;1;4m" + "es konnten keine Ergebnisse gefunden werden" + "\033[0m")
