import requests

# Url of Weather Underground Location
url = "https://www.wunderground.com/weather/us/oh/youngstown"

# Send an HTTP request to fetch the html content of the page.
response = requests.get(url)

#print the status code
print(f"Status Code: {response.status_code}")