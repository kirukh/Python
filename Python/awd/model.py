import json
import csv
import sys

def read_websites_config():
	website_dict = {}
	websites = []
	
	try:
		with open("config.json", "r") as file:
			website_dict = json.loads(file.read())
	except FileNotFoundError:
		print("\033[31;1;4m" + "config.json wurde nicht gefunden.\nerstelle datei..." + "\033[0m")
		with open("config.json", "w") as file:
			config_content = {
				"National Geographic": "https://www.nationalgeographic.de/",
				"Spektrum": "https://www.spektrum.de/",
				"Tagesschau": "https://www.tagesschau.de/wissen",
				"Forschung und Wissen": "https://www.forschung-und-wissen.de/"
			}
			json.dump(config_content, file, indent=4)
		print("\033[31;1;4m" + "config.json wurde erstellt.\nBitte rufe den Scraper erneut auf" + "\033[0m")
		sys.exit()	 
	except Exception as e:
		print("\033[2J\033[H")
		print("\033[31;1;4m" + str(e) + "\033[0m")
	
	return website_dict

def save_output(content, filename):
	filename += ".csv"
	
	try:
		with open(filename, "w", encoding="utf-8-sig", newline="") as file:
			csvwriter = csv.writer(file, delimiter=",")
			for line in content:
				line = [line, ""]
				csvwriter.writerow(line)
	except Exception as e:
		print("\033[2J\033[H")
		print("\033[31;1;4m" + str(e) + "\033[0m")

def read_cache():
	cache_name = "web_scraper_cache.json"
	cache_content = ""
	try:
		with open(cache_name, "r") as file:
			cache_content = json.loads(file.read())
	except Exception as e:
		print("\033[31;1;4m" + str(e) + "\033[0m")
		cache_content = {}
	return cache_content
	
def write_cache(content):
	cache_name = "web_scraper_cache.json"
	
	try:
		with open(cache_name, "w") as file:
			json.dump(content, file, indent=4)
	except Exception as e:
		print("\033[2J\033[H")
		print("\033[31;1;4m" + str(e) + "\033[0m")