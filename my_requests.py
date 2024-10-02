import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
# response = requests.get("https://google.com")

# print(response.json())
print(response.status_code)
# print(response.headers)
# print(response.text)

data = response.json()
# print(data)
print("Name: ", data['name'])
print("Height: ", data['height'])
print("Weight: ", data['weight'])
print("Abilities: ", [ability['ability']['name'] for ability in data ['abilities']])