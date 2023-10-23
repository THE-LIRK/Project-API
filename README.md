# Pokémon Data Project 🐱‍🏍
 
![Capture d'écran 2023-10-23 105026](https://github.com/THE-LIRK/Project-API/assets/121623903/c5d3cf8e-e27a-4643-adad-251577901eca)

## Description 📝

Ce projet est une application web qui permet de collecter, stocker et rechercher des données sur les Pokémon. Il utilise plusieurs technologies clés pour offrir une expérience utilisateur complète.

## Fonctionnalités 🚀

- **Récupération de données depuis l'API Pokémon** : L'application récupère les données sur les Pokémon depuis l'API Pokémon (pokeapi.co).

- **Stockage des données avec Elasticsearch** : Toutes les données des Pokémon sont stockées dans une base de données Elasticsearch. Elasticsearch est une base de données NoSQL qui permet une recherche rapide et flexible.

- **API avec FastAPI** : FastAPI est un framework web pour Python qui facilite la création d'API RESTful. L'application utilise FastAPI pour exposer des endpoints qui permettent de rechercher des Pokémon par leur nom, leurs capacités, etc.

- **Interface utilisateur avec Streamlit** : Streamlit est un outil pour créer des applications web simples et interactives en Python. L'application utilise Streamlit pour créer une interface utilisateur conviviale où les utilisateurs peuvent effectuer des recherches, afficher les détails des Pokémon et ajouter de nouveaux Pokémon.

- **Visualisation avec Kibana (facultatif)** : Si vous le souhaitez, vous pouvez utiliser Kibana, un outil de visualisation de données, pour explorer et visualiser les données Pokémon stockées dans Elasticsearch. Kibana offre des fonctionnalités de tableau de bord et de création de graphiques pour analyser les données.

## Configuration requise 🛠

- Python 3.x
- Bibliothèques Python (FastAPI, Elasticsearch, Requests, Streamlit)
- Compte Elasticsearch pour le stockage des données.
- (Facultatif) Kibana pour la visualisation des données.

## Installation 📦

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/THE-LIRK/Project-API.git
   ```

2. Installez les dépendances Python :

   ```bash
   pip install -r requirements.txt
   ```

3. Configurez Elasticsearch avec l'URL de votre instance Elasticsearch dans le fichier `extract.py`.

4. Exécutez l'application FastAPI :

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

5. Accédez à l'application dans votre navigateur à l'adresse http://localhost:8000.

6. Lancement de Streamlit :

   ```bash
   streamlit run streamlit_app.py
   ```

7. Accédez à l'interface Streamlit dans votre navigateur à l'adresse http://localhost:8501.

## Documentation FastAPI 📄

- Pour accéder à la documentation de l'API FastAPI, ouvrez votre navigateur et visitez http://localhost:8000/docs. Vous trouverez des informations détaillées sur les endpoints les fonctionnalités de l'API et faire des tests.

## Utilisation 🕹

- Utilisez l'interface Streamlit pour rechercher des Pokémon par nom, capacité, etc.
- Ajoutez de nouveaux Pokémon en utilisant l'interface Streamlit.
- Supprimez un Pokémon par son ID en utilisant l'endpoint FastAPI `/pokemon/{pokemon_id}` avec DELETE.

- (Facultatif) Utilisez Kibana pour visualiser les données stockées dans Elasticsearch.

## Auteur ✍️
- roddy-keonny.lepenguet-itsoma.edu@groupe-gema.com
- linkedin.com/in/roddy-keonny
