import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '40895432dc82a2faf146707e400f28b3'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_confirmation = {
    "trainer_token" : TOKEN
}
body_create = {
    "name": "generate",
    "photo_id": 1
}
body_change = {
    "pokemon_id": "189924",
    "name": "Никита",
    "photo_id": 2
}
body_add = {
    "pokemon_id": "189924"
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json())

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.json())

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.json())