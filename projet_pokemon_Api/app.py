import streamlit as st
import requests

# URL de l'API FastAPI
api_url = "http://127.0.0.1:8000" 


# Page 1 : Rechercher un Pokémon par ID
def search_pokemon_by_id():
    st.title("Rechercher un Pokémon par ID")
    id_pokemon = st.number_input("ID du Pokémon")
    if st.button("Rechercher"):
        response = requests.get(f"{api_url}/pokemon/search/id?id_pokemon={id_pokemon}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Pokémon non trouvé")


# Page 2 : Rechercher un Pokémon par nom
def search_pokemon_by_name():
    st.title("Rechercher un Pokémon par nom")
    name = st.text_input("Nom du Pokémon")
    if st.button("Rechercher"):
        response = requests.get(f"{api_url}/pokemon/search/?name={name}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Pokémon non trouvé")

# Page 3 : Rechercher des Pokémon par capacité
def search_pokemon_by_ability():
    st.title("Rechercher des Pokémon par capacité")
    ability_name = st.text_input("Nom de la capacité")
    if st.button("Rechercher"):
        response = requests.get(f"{api_url}/pokemon/by_ability/?ability_name={ability_name}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Aucun Pokémon avec cette capacité")

# Page 4 : Ajouter un nouveau Pokémon
def add_new_pokemon():
    st.title("Ajouter un nouveau Pokémon")

    # Créez des champs de saisie pour les informations du Pokémon
    id=st.number_input("id")
    name = st.text_input("Nom du Pokémon")
    base_experience = st.number_input("Expérience de base")
    hp = st.number_input("HP")
    attack = st.number_input("Attaque")
    defense = st.number_input("Défense")
    special_attack = st.number_input("Attaque spéciale")
    special_defense = st.number_input("Défense spéciale")
    height = st.number_input("Taille")
    weight = st.number_input("Poids")

    # Créez des champs de saisie pour les capacités (peut y avoir plusieurs)
    abilities = st.text_input("Capacités (séparées par des virgules)").split(',')

    # Créez des champs de saisie pour les mouvements (peut y avoir plusieurs)
    moves = st.text_input("Mouvements (séparés par des virgules)").split(',')

    # Créez un champ de saisie pour le type (peut y avoir plusieurs)
    type = st.text_input("Type (séparés par des virgules)").split(',')

    if st.button("Ajouter le Pokémon"):
        # Créez un dictionnaire avec les données du nouveau Pokémon
        new_pokemon = {
            "id":id,
            "name": name,
            "base_experience": base_experience,
            "height": height,
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "special_attack": special_attack,
            "special_defense": special_defense,
            "abilities": abilities,
            "weight": weight,                                 
            "moves": moves,
            "type": type
        }

        # Envoyez les données du nouveau Pokémon à l'API FastAPI pour l'ajout
        response = requests.post(f"{api_url}/pokemon/",json=new_pokemon)

        if response.status_code == 200:
            st.success("Pokémon ajouté avec succès")
        else:
            st.error("Erreur lors de l'ajout du Pokémon")



# Page 5 : Supprimer un Pokémon par ID
def delete_pokemon_by_id():
    st.title("Supprimer un Pokémon par ID")
    id_to_delete = st.number_input("ID du Pokémon à supprimer")
    if st.button("Supprimer"):
        response = requests.delete(f"{api_url}/pokemon/{id_to_delete}")
        if response.status_code == 200:
            st.success("Pokémon supprimé avec succès")
        else:
            st.error("Pokémon non trouvé ou erreur lors de la suppression")



# Sélection de la page via une barre latérale
page = st.sidebar.selectbox(
    "Sélectionnez une page",
    ["Rechercher par ID", "Rechercher par nom", "Rechercher par capacité", "Ajouter un Pokémon", "Supprimer par ID"]
)

if page == "Rechercher par ID":
    search_pokemon_by_id()
elif page == "Rechercher par nom":
    search_pokemon_by_name()
elif page == "Rechercher par capacité":
    search_pokemon_by_ability()
elif page == "Ajouter un Pokémon":
    add_new_pokemon()
elif page == "Supprimer par ID":
    delete_pokemon_by_id()
