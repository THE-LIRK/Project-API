import requests
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=["http://localhost:9200"])

# Récupération de la liste des 100 premiers Pokémon
res = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=100")
data = res.json()
results = data['results']

index_name = "pokemon_data"
es.indices.create(index=index_name, ignore=400)

total = []

# Boucle pour récupérer les données de chaque Pokémon
for item in results:
    url = item['url']
    data = requests.get(url).json()
    
    id = data['id']
    name = data['name']
    base_experience = data["base_experience"]
    abilities = data["abilities"]
    height = data["height"]
    weight = data["weight"]
    moves = data["moves"]
    types = data["types"]
    stats = data["stats"]
    
    # Créer des ensembles pour stocker les noms des capacités, mouvements et types uniques
    ability_names = set()
    moves_names = set()
    type_name = set()
    
    for sta in stats:
        stat_name = sta["stat"]["name"]
        base_stat = sta["base_stat"]

        if stat_name == "hp":
            hp = base_stat
        if stat_name == "attack":
            attack = base_stat
        if stat_name == "defense":
            defense = base_stat
        if stat_name == "special-attack":
            special_attack = base_stat
        if stat_name == "special-defense":
            special_defense = base_stat

    for type in types:
        typ = type["type"]["name"]
        type_name.add(typ)
    
    for ability in abilities:
        abn = ability["ability"]["name"]
        ability_names.add(abn)

    for move in moves:
        mov = move["move"]["name"]
        moves_names.add(mov)

    pokemon_info = {
        'id': id,
        'name': name,
        'base_experience': base_experience,
        'hp': hp,
        'attack': attack, 
        'defense': defense,
        'special_attack': special_attack,
        'special_defense': special_defense,
        'abilities': list(ability_names),
        'height': height,
        'weight': weight,
        'moves': list(moves_names), 
        'type': list(type_name)  
    }
    
    total.append(pokemon_info)

for pokemon in total:
    es.index(index=index_name, body=pokemon)
