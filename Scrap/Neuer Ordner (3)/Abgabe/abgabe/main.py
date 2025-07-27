from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import control

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
	return FileResponse("static/index.html")
	
@app.get("/api/websites")
def get_websites():
	return control.get_websites()
	
@app.get("/api/headlines/{website_name}")
def get_headlines(website_name: str, filter: str = None):
	titles = []
	
	if website_name == "National Geographic":
		titles = control.connect_to_national_geographic()
	elif website_name == "Spektrum":
		titles = control.connect_to_spektrum()
	elif website_name == "Tagesschau":
		titles = control.connect_to_tagesschau()
	elif website_name == "Forschung und Wissen":
		titles = control.connect_to_forschung_und_wissen()
	else:
		raise HTTPException(status_code=404, detail="Website nicht gefunden")
		
	if not titles:
		raise HTTPException(status_code=500, detail="Keine Titel gefunden")
	
		titles = list(set([title.lower().strip() for title in titles if title]))

	if filter:
		titles = control.filter_titles(titles, filter.lower())
	
	return {"headlines": titles}
