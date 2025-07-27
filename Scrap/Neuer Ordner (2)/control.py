import model
import requests
from bs4 import BeautifulSoup
import datetime
import sys

def get_websites():
	return model.read_websites_config()

#Funktion zum Verbindungsaufbau mit einer gegebenen website
#gibt html code als BeautifulSoup objekt zurück
def get_html(url):
	
	try:
		headers = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
		request = requests.get(url, headers=headers)
		request.encoding = "utf-8"
	except requests.exceptions.ConnectionError:
		print("\033[2J\033[H")
		print("\033[31;1;4m" + "Verbindung zur Website konnte nicht hergestellt werden" + "\033[0m")
		sys.exit()
	except requests.exceptions.Timeout:
		print("\033[2J\033[H")
		print("\033[31;1;4m" + "Verbindungs Timeout" + "\033[0m")
		sys.exit()
	except requests.exceptions.RequestExcpetion as e:
		print("\033[2J\033[H")
		print("\033[31;1;4m" + "Unbekannter Fehler:" + "\033[0m")
		print("\033[31;1;4m" + str(e) + "\033[0m")
		sys.exit()
	print("Verbindung wurde hergestellt")
	return BeautifulSoup(request.text, features="html.parser")

#Funktion zum Erstellen des Cache
def write_cache(website, content):
	current_datetime = datetime.datetime.now()
	output = {
		"timestamp": current_datetime.isoformat(),
		"website": str(website),
		"scraped_content": content
	}
	
	model.write_cache(output)
	
#Funktion zum Lesen des Cache
def read_cache(website):
	current_datetime = datetime.datetime.now()
	cache = model.read_cache()
	connection_needed = True
	content = []
	if cache:
		cached_timestamp = datetime.datetime.fromisoformat(cache["timestamp"])
		cached_website = cache["website"]
		if website == cached_website:
			if (current_datetime - cached_timestamp) < datetime.timedelta(minutes=30):
				connection_needed = False
				content = cache["scraped_content"]
			else:
				connection_needed = True
				
		else:
			connection_needed = True
			
	return connection_needed, content

#Funktion zum Filtern der Titel
def filter_titles(titles, filter_str):
	if filter_str:
		#Falls der jeweilige Titel den Teilstring des Users enthält, wird der Titel ausgegeben
		return [title for title in titles if filter_str in title]
	else:
		return titles
			
#Die ganzen Website spezifischen Funktionen zum scrapen der Überschriften	
def connect_to_national_geographic():
	connection_needed, cache = read_cache("www.nationalgeographic.de")
	if connection_needed:
		urls = ["https://www.nationalgeographic.de/geschichte-und-kultur", "https://www.nationalgeographic.de/tiere", "https://www.nationalgeographic.de/wissenschaft", "https://www.nationalgeographic.de/umwelt", "https://www.nationalgeographic.de/reise-und-abenteuer"]
		contents = []
		
		for url in urls:
			contents.append(get_html(url))
		
		titles = []
		
		for content in contents:
			h2_tags = content.find_all("h2")
			for h2_tag in h2_tags:
				titles.append(h2_tag.string)
				
		write_cache("www.nationalgeographic.de", titles)
	else:
		titles = cache
			
	return titles

def connect_to_spektrum():
	connection_needed, cache = read_cache("www.spektrum.de")
	if connection_needed:
		urls = [
			"https://www.spektrum.de/news/astronomie/",
			"https://www.spektrum.de/news/biologie/",
			"https://www.spektrum.de/news/chemie/",
			"https://www.spektrum.de/news/erde-umwelt/",
			"https://www.spektrum.de/news/technik/",
			"https://www.spektrum.de/news/kultur/",
			"https://www.spektrum.de/news/mathematik/",
			"https://www.spektrum.de/news/medizin/",
			"https://www.spektrum.de/news/physik/",
			"https://www.spektrum.de/news/psychologie-hirnforschung/"
		]
		
		contents = []
		
		for url in urls:
			contents.append(get_html(url))
			
		titles = []
		
		for content in contents:
			#artikel ganz oben auf jeder seite
			h2_tags = content.find_all("h2")
			for h2_tag in h2_tags:
				text = h2_tag.string
				if text != "Fachgebiete" and text != "Services":
					titles.append(text)
		
			#andere artikel auf seite
			h3_tags = content.find_all("h3")
			
			for h3_tag in h3_tags:
				spans = h3_tag.find_all("span")
				
				if len(spans) == 3:
					titles.append(spans[2].string)
					
		write_cache("www.spektrum.de", titles)
	else:
		titles = cache
	return titles	
	

def connect_to_tagesschau():
	connection_needed, cache = read_cache("www.tagesschau.de")
	if connection_needed:
		url = "https://www.tagesschau.de/wissen"
		content = get_html(url)
		
		titles = []
		spans = content.find_all("span", class_="teaser-xs__headline")
		for span in spans:
			titles.append(span.text.strip())
		write_cache("www.tagesschau.de", titles)
	else:
		titles = cache		
	return titles
	
def connect_to_forschung_und_wissen():
	connection_needed, cache = read_cache("www.forschung-und-wissen.de")
	if connection_needed:
		url = "https://www.forschung-und-wissen.de/"
		content = get_html(url)
		
		titles = []
		h3_tags = content.find_all("h3", class_="headline")
		for h3_tag in h3_tags:
			links = h3_tag.find_all("a")
			if len(links) == 1:
				titles.append(links[0].text.strip())
		write_cache("www.forschung-und-wissen.de", titles)
	else:
		titles = cache
	return titles	

#Funktion zum speichern des Outputs	
def save_output(content, filename):
	#Wenn nichts gefunden wurde, dann gib "Keine Ergebnisse gefunden!" aus. Ansonstten das gefundene
	content = content if content else ["Keine Ergebnisse gefunden!"]
	model.save_output(content, filename)
