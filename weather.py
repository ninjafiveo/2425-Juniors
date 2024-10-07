import requests
from bs4 import BeautifulSoup

# Url of Weather Underground Location
url = "https://www.wunderground.com/weather/us/oh/youngstown"
# url = "https://regionalchamber.com/"

# Send an HTTP request to fetch the html content of the page.
response = requests.get(url)

# Initialize BeautifulSoup to parse the html content
soup = BeautifulSoup(response.text, "html.parser")


#print the status code
print(f"Status Code: {response.status_code}")
# Print the parsed HTML (This is optional to see the structure of the page.)
# print(soup.prettify())

# temperature_element = soup.find("span", class_="wu-value wu-value-to")
temperature_element = soup.find_all("span", class_="wu-value wu-value-to")
# print(temperature_element)

# temperature = temperature_element.text if temperature_element else "N/A"

for element in temperature_element:
    print(element.text)


# print(f"Current Temp: {temperature}°")