document.addEventListener('DOMContentLoaded', () => {
	const button = document.getElementById("submit");
	const websiteSelect = document.getElementById("website-select");
	const filter = document.getElementById("filter-input");
	const results = document.getElementById("results");
	
	window.addEventListener("load", async () => {
		const response = await fetch("/api/websites");
		const websites = await response.json();
		
		for (const website in websites) {
			const option = document.createElement("option");
			option.value = website;
			option.textContent = website;
			websiteSelect.appendChild(option);
		}
	});
	
	
	button.addEventListener("click", async (event) => {
		event.preventDefault();
		results.innerHTML = "<p>Lade Schlagzeilen</p>";
		
		const selectedWebsite = websiteSelect.value;
		const filterValue = filter.value;
		
		let api = `/api/headlines/${selectedWebsite}`;
		if (filterValue) {
			api += `?filter=${filterValue}`;
		}
		
		try {
			const response = await fetch(api);
			
			if (!response.ok) {
				const errorData = await response.json();
				throw new Error(errorData.detail || "Fehler");
			}
			
			const data = await response.json();
			
			if (data.headlines && data.headlines.length > 0) {
				const ul = document.createElement("ul");
				data.headlines.forEach(headline => {
					const li = document.createElement("li");
					li.textContent = headline;
					ul.appendChild(li);
				});
				results.innerHTML = "";
				results.appendChild(ul);
			} else {
				results.innerHTML = "<p>Keine Schlagzeilen gefunden</p>";
			} 
		} catch (error) {
			console.log(`Fehler: ${error.message}`);
		}		
	});
		
	
});
