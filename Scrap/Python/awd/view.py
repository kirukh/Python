import control
import questionary
from prettytable import PrettyTable

def print_output_table(content):
	print("\033[0m\033[2J\033[H\033[0m")
	table = PrettyTable()
	table.field_names = ["Artikel Überschrift"]
	if content:
		for element in content:
			table.add_row([element])
	else:
		table.add_row(["Keine Ergebnisse gefunden!"])
	print(table)

websites = control.get_websites()
answers = questionary.form(first = questionary.select("Von welcher Webseite soll gescraped werden: ", choices = [i for i in websites.keys()]), second = questionary.text("Nach welchen wörtern möchtet du filtern (optional): "), third = questionary.text("Bitte gib einen Dateinamen zum Speichern der Ergebniss ein: ")).ask()

titles = []
filter_input = answers["second"]

if answers["first"] == "National Geographic":
	titles = control.connect_to_national_geographic(filter_input)
elif answers["first"] == "Spektrum":
	titles = control.connect_to_spektrum(filter_input)
elif answers["first"] == "Tagesschau":
	titles = control.connect_to_tagesschau(filter_input)
elif answers["first"] == "Forschung und Wissen":
	titles = control.connect_to_forschung_und_wissen(filter_input)

if titles:
	titles_for_output = list(set([title.lower().strip() for title in titles]))
	print_output_table(titles_for_output)
	if answers["third"]:
		control.save_output(titles_for_output, answers["third"])
	else:
		print("\033[31;1;4m" + "keine datei zum Speichern ausgewählt" + "\033[0m")
			
else:
	print("\033[31;1;4m" + "es konnten keine Ergebnisse gefunden werden" + "\033[0m")