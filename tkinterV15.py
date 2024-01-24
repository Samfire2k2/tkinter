from tkinter import *
from PIL import ImageTk,Image
import requests
import json


root = Tk() # Créer une nouvelle fenêtre tkinter
root.title("Weather App")
root.iconbitmap('C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico')
root.geometry("900x100")

#Create Zipcode Lookup Function
def zipLookup():
	zip.get()
#	zipLabel = Label(root, text=zip.get())
#	zipLabel.grid(row=1, column=0, columnspan=2)

	try:
		api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zip.get() + "&date=2024-01-24&distance=900&API_KEY=8C04ABCF-A0E1-450E-AE11-605297AFA186")
##		print(json.loads(api_request.content))
		api = json.loads(api_request.content)
		city = api[0]['ReportingArea']
		state = api[0]['StateCode']
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']

		if category == "Good":
			weather_color = "#00e400"
		elif category == "Moderate":
			weather_color = "#FFFF00"
		elif category == "Unhealthy for Sensitive Groups":
			weather_color = "#ff7e00"
		elif category == "Unhealthy":
			weather_color = "#FF0000"
		elif category == "Very Unhealthy":
			weather_color = "#8f3f97"
		elif category == "Hazardous":
			weather_color = "#7e0023"


		root.configure(background=weather_color)
		
		myLabel = Label(root, text=city + " " + state + " Qualité de l'air " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color) 
		myLabel.grid(row=1, column=0, columnspan=2)
	except Exception as e:	
		api = "Code postal non valide"
		print(api)


zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(root, text="Code Postal", command=zipLookup)
zipButton.grid(row=0, column=1, sticky=W+E+N+S)


root.mainloop()