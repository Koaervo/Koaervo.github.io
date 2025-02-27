import requests
import json

def Get_Data():
    The_id = input("Enter Pokémon ID: ")

    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{The_id}/"
    response_pokemon = requests.get(pokemon_url)
    
    if response_pokemon.status_code != 200:
        print("Error: Unable to fetch Pokémon data")
        return
    
    pokemon_data = response_pokemon.json()

    form_url = f"https://pokeapi.co/api/v2/pokemon-form/{The_id}/"
    response_form = requests.get(form_url)
    
    if response_form.status_code != 200:
        print("Error: Unable to fetch Pokémon form data")
        return
    
    form_data = response_form.json()
    
    result = {
        "stats": pokemon_data.get("stats"),
        "name": form_data.get("name"),
        "sprite": form_data.get("sprites", {})
    }
    
    print(json.dumps(result, indent=4))

Get_Data()
