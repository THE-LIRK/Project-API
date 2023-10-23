from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from elasticsearch import Elasticsearch
from pydantic import BaseModel
from typing import List



app = FastAPI()

# Connexion à Elasticsearch
es = Elasticsearch(hosts=["http://localhost:9200"])
index_name = "pokemon_data"


    
class pokemon_data(BaseModel):
    id: int 
    name: str
    base_experience: int
    height: int
    hp:int
    attack: int 
    defense: int
    special_attack:int
    special_defense:int
    abilities: List[str] 
    height: int
    weight: int
    moves:list[str]
    type:list[str]


    


# Endpoint pour rechercher des Pokémon par leur id
@app.get("/pokemon/search/id")
async def search_pokemonid(id_pokemon:int):
    query= {"query":
            {"match":{

                "id":id_pokemon

            }}}
    
    response=es.search(index=index_name , body=query)
    results = [hit["_source"] for hit in response["hits"]["hits"]]
    return JSONResponse(content=results, status_code=200)
    

    
# Endpoint pour rechercher des Pokémon par leur nom
@app.get("/pokemon/search/")
async def search_pokemon(name: str):
    query = {"query": {
                    "match": {
                        "name": name
                    }
                }
            }
    
    response = es.search(index=index_name, body=query)
    if response['hits']['total']['value'] == 0:
                    # Aucun Pokémon avec cet ID n'a été trouvé, renvoyez une réponse 404
            raise HTTPException(status_code=404, detail="Pokémon non trouvé")
    
    results = [hit["_source"] for hit in response["hits"]["hits"]]
    return JSONResponse(content=results, status_code=200)




# Endpoint pour rechercher les Pokémon par capacité
@app.get("/pokemon/by_ability/")
async def search_pokemon_by_ability(ability_name: str):
    query = {
        "query": {
            "match": {
                "abilities": ability_name
            }
        }
    }
    
    response = es.search(index=index_name, body=query)
    results = [hit["_source"]["name"] for hit in response["hits"]["hits"]]
    
    if results:
        return {"pokemons_with_ability": results}
    else:
        raise HTTPException(status_code=404, detail=f"Aucun Pokémon n'a la capacité '{ability_name}'")




# Endpoint pour ajouter un nouveau Pokémon
@app.post("/pokemon/")
async def add_pokemon(data: pokemon_data):
    # Créez un dictionnaire avec les données du Pokémon
    new_pokemon_data = {
    'id': data.id, 
    'name': data.name,
    'base_experience': data.base_experience,
    'height': data.height,
    'hp':data.hp,
    'attack': data.attack, 
    'defense': data.defense,
    'special_attack':data.special_attack,
    'special_defense':data.special_defense,
    'abilities': data.abilities,
    'weight': data.weight,
    'moves':data.moves,
    'type':data.type
    }


    # Recherchez si un document avec le même ID existe déjà
    query = {
        "query": {
            "term": {
                "id": data.id
            }
        }
    }
    
    response = es.search(index=index_name, body=query)
    if response['hits']['total']['value'] == 0:
        # Aucun document avec le même ID n'a été trouvé, ajoutez le Pokémon
        es.index(index=index_name, body=new_pokemon_data)
        return {"message": "Pokémon ajouté avec succès", "data": new_pokemon_data}
    else:
        # Un document avec le même ID existe déjà, renvoyez une erreur
        raise HTTPException(status_code=400, detail=f"L'ID '{data.id}' existe déjà. Les IDs doivent être uniques.")


# Endpoint pour supprimer un Pokémon par son ID
@app.delete("/pokemon/{pokemon_id}")
async def delete_pokemon(pokemon_id: int):
    try:
        # Recherchez le Pokémon avec l'ID spécifié
        query = {
            "query": {
                "term": {
                    "id": pokemon_id
                }
            }
        }
        response = es.search(index=index_name, body=query)
        
        if response['hits']['total']['value'] == 0:
            # Aucun Pokémon avec cet ID n'a été trouvé, renvoyez une réponse 404
            raise HTTPException(status_code=404, detail="Pokémon non trouvé")
        
        # Si un Pokémon avec cet ID a été trouvé, supprimez-le
        for hit in response['hits']['hits']:
            es.delete(index=index_name, id=hit['_id'])
        
        return {"status": "Pokémon supprimé"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Une erreur s'est produite lors de la suppression du Pokémon.")


    



