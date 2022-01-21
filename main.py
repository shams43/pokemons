import requests

pokemons = dict()
f = False
class Pokemon:
    def __init__(self, name):
        # проверяем на наличие в словаре

        if name in pokemons:
            pok = pokemons[name]
            print(*pok.a, sep=', ')
        else:
            f = True
            url = "https://pokeapi.co/api/v2/pokemon/{id or name}/"
            url = url.replace("{id or name}", name)
            req = requests.get(url)
            if req.status_code == 404:
                print("Такого покемона не существует, дебил.")
                return None
            poke = req.json()
            self.a = []
            self.name = name
            for i in poke["abilities"]:
                self.a.append(i["ability"]["name"])
            print(*self.a, sep=", ")

while True:
    inp = input()
    if inp == "get":
        print('Имя покемона: ')
        name = input()
        pokemon = Pokemon(name)
        if f:
            pokemons[name] = pokemon
        print()
    else:
        print("Такой команды не существует, дебил.")
