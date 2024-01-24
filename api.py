import requests

url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=44120&distance=5&API_KEY=8C04ABCF-A0E1-450E-AE11-605297AFA186"
response = requests.get(url)

print(response.status_code)
print(response.json())  # Si la réponse est au format JSON


#200 - OK