import model
import requests
from bs4 import BeautifulSoup
import datetime
import sys
import re

def get_websites():
	return model.read_websites_config()

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
	except requests.exceptions.RequestException as e:
		print("\033[2J\033[H")
		print("\033[31;1;4m" + "Unbekannter Fehler:" + "\033[0m")
		print("\033[31;1;4m" + str(e) + "\033[0m")
		sys.exit()
	print("Verbindung wurde hergestellt")
	return BeautifulSoup(request.text, features="html.parser")

def write_cache(website, content):
	current_datetime = datetime.datetime.now()
	output = {
		"timestamp": current_datetime.isoformat(),
		"website": str(website),
		"scraped_content": content
	}
	
	model.write_cache(output)
	
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
			
def connect_to_national_geographic(filter_str):
	connection_needed, cache = read_cache("www.nationalgeographic.de")
	if connection_needed:
		urls = ["https://www.nationalgeographic.de/geschichte-und-kultur", "https://www.nationalgeographic.de/tiere", "https://www.nationalgeographic.de/wissenschaft", "https://www.nationalgeographic.de/umwelt", "https://www.nationalgeographic.de/reise-und-abenteuer"]
		
		titles = []
		
		for url in urls:
			soup = get_html(url)
			html_content = str(soup)

			h1_pattern = r"<h1[^>]*>(.*?)</h1>"
			h2_pattern = r"<h2[^>]*>(.*?)</h2>"
			h3_pattern = r"<h3[^>]*>(.*?)</h3>"
			
			found_titles = re.findall(h1_pattern, html_content, re.IGNORECASE | re.DOTALL)
			found_titles.extend(re.findall(h2_pattern, html_content, re.IGNORECASE | re.DOTALL))
			found_titles.extend(re.findall(h3_pattern, html_content, re.IGNORECASE | re.DOTALL))
			
			titles.extend(found_titles)
			
		filtered_titles = []
		if filter_str:
			for title in titles:
				if filter_str.lower() in title.lower():
					filtered_titles.append(title)
		else:
			filtered_titles = titles
				
		write_cache("www.nationalgeographic.de", filtered_titles)
	else:
		titles = cache
			
	return titles

def connect_to_spektrum(filter_str):
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
		
		titles = []
		
		for url in urls:
			soup = get_html(url)
			html_content = str(soup)

			h1_pattern = r"<h1[^>]*>(.*?)</h1>"
			h2_pattern = r"<h2[^>]*>(.*?)</h2>"
			h3_pattern = r"<h3[^>]*>(.*?)</h3>"
			
			found_titles = re.findall(h1_pattern, html_content, re.IGNORECASE | re.DOTALL)
			found_titles.extend(re.findall(h2_pattern, html_content, re.IGNORECASE | re.DOTALL))
			found_titles.extend(re.findall(h3_pattern, html_content, re.IGNORECASE | re.DOTALL))
			
			titles.extend(found_titles)
			
		filtered_titles = []
		if filter_str:
			for title in titles:
				if filter_str.lower() in title.lower():
					filtered_titles.append(title)
		else:
			filtered_titles = titles
					
		write_cache("www.spektrum.de", filtered_titles)
	else:
		titles = cache
	return titles	
	
def connect_to_tagesschau(filter_str):
	connection_needed, cache = read_cache("www.tagesschau.de")
	if connection_needed:
		url = "https://www.tagesschau.de/wissen"
		soup = get_html(url)
		html_content = str(soup)
		
		titles = []
		
		h1_pattern = r"<h1[^>]*>(.*?)</h1>"
		h2_pattern = r"<h2[^>]*>(.*?)</h2>"
		h3_pattern = r"<h3[^>]*>(.*?)</h3>"
		
		found_titles = re.findall(h1_pattern, html_content, re.IGNORECASE | re.DOTALL)
		found_titles.extend(re.findall(h2_pattern, html_content, re.IGNORECASE | re.DOTALL))
		found_titles.extend(re.findall(h3_pattern, html_content, re.IGNORECASE | re.DOTALL))
		
		titles.extend(found_titles)
		
		filtered_titles = []
		if filter_str:
			for title in titles:
				if filter_str.lower() in title.lower():
					filtered_titles.append(title)
		else:
			filtered_titles = titles

		write_cache("www.tagesschau.de", filtered_titles)
	else:
		titles = cache		
	return titles
	
def connect_to_forschung_und_wissen(filter_str):
	connection_needed, cache = read_cache("www.forschung-und-wissen.de")
	if connection_needed:
		url = "https://www.forschung-und-wissen.de/"
		soup = get_html(url)
		html_content = str(soup)
		
		titles = []

		h1_pattern = r"<h1[^>]*>(.*?)</h1>"
		h2_pattern = r"<h2[^>]*>(.*?)</h2>"
		h3_pattern = r"<h3[^>]*>(.*?)</h3>"
		
		found_titles = re.findall(h1_pattern, html_content, re.IGNORECASE | re.DOTALL)
		found_titles.extend(re.findall(h2_pattern, html_content, re.IGNORECASE | re.DOTALL))
		found_titles.extend(re.findall(h3_pattern, html_content, re.IGNORECASE | re.DOTALL))
		
		titles.extend(found_titles)
		
		filtered_titles = []
		if filter_str:
			for title in titles:
				if filter_str.lower() in title.lower():
					filtered_titles.append(title)
		else:
			filtered_titles = titles

		write_cache("www.forschung_und_wissen.de", filtered_titles)
	else:
		titles = cache
	return titles	

def save_output(content, filename):
	content = content if content else ["Keine Ergebnisse gefunden!"]
	model.save_output(content, filename)