from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        for current_pokemon in self.pokemons:
            if current_pokemon.name == pokemon.name:
                return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        for current_pokemon in self.pokemons:
            if current_pokemon.name == pokemon_name:
                self.pokemons.remove(current_pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]

        for pokemon in self.pokemons:
            result.append(f"- {pokemon.pokemon_details()}")

        return "\n".join(result)
