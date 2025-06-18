import requests
import os

def descargar_cry(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"

    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()

        nombre = data["name"]
        cry_url = data.get("cries", {}).get("latest")

        if not cry_url:
            print(f" {nombre} no tiene cry disponible.")
            return

        os.makedirs("cries", exist_ok=True)
        ruta = f"cries/{nombre}.ogg"

        sonido = requests.get(cry_url)
        with open(ruta, "wb") as f:
            f.write(sonido.content)

        print(f" Cry de {nombre} descargado como {ruta}")
    except Exception as e:
        print(f" Error: {e}")


def mostrar_menu_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon"

    params = {
        "limit": 150,
        "offset": 0
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        pokemon_list = data['results']

        for i, pokemon in enumerate(pokemon_list, start=1):
            print(f"{i}: {pokemon['name'].capitalize()}")

        return pokemon_list  # Return the list of Pokemon
    else:
        print("Error al obtener los datos:", response.status_code)
        return None


if __name__ == "__main__":
    while True:
        print("\n--- Menú ---")
        print("1. Listar Pokémon")
        print("2. Descargar Cry de Pokémon (por ID)")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            pokemon_list = mostrar_menu_pokemon()
            if pokemon_list:
                print("\nPokémon listados.")

        elif opcion == "2":
            id_pokemon = input("Introduce el ID del Pokémon: ")
            descargar_cry(id_pokemon)

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

