# Exercice technique Inthy

Pour instancier le modele de base de donnée au lancement :
`sudo docker compose exec api python init_db.py`

Pour integrer les données dans la base de données :
- mettre un csv dans un dossier data à la racine du projet
- `sudo docker compose exec api python -m consumption_app.utils.import_data`

## TODO

- Factoriser les variables d'envirronnement et les mettre dans un .env
- Intégrer l'initialisation de la db au lancement du docker
- Ajouter au script d'import la possibilité de lire les xls
- Ignorer le nommage du fichier de donnée dans le script d'import
- Créer un cron pour la récupération des export de consommation
- Ajouter un test pour le controlleur qui vérifie la bonne gestions des erreurs de validation et le bon retour de données
- Modifier la structure des dossier, le repository abstrait et les entités devraient etre dans un dossier domain


## Exercice avec préparation (4h de préparation maximum)

RTE fournit les données de consommation énergétique et du mix énergétique français
dans le passé sur le site suivant:
https://www.rte-france.com/eco2mix/telecharger-les-indicateurs.

### Votre mission si vous l’acceptez
-​ Télécharger les données annuelles de consommation (en puissance) depuis le
site. Les seules données qui nous intéressent sont la puissance totale
consommée en France demi-heure par demi-heure.

- Choisir un schéma de base de données relationnelle adapté au stockage de ces
données, de manière à pouvoir les stocker et les requêter de manière efficace
dans la suite de l’exercice.

    ○​  Écrire une requête SQL qui répond à la question: quelle était la
    consommation moyenne entre le 1er janvier à 6h et le 3 à 17h ?

    -> `SELECT AVG(consumption) as AVG_CONS_MW FROM energy WHERE date BETWEEN '01/01/2025 06:00:00' AND '03/01/2025 17:00:00';`

- Insérer les données dans une base de données locale de votre choix selon le
schéma choisi à l’aide d’un script python.

- Créer une API en python qui contiendra un seul endpoint et permettra de
requêter les données depuis la base de données créée à l’étape précédente.
L’API doit prendre en paramètre une date et une heure de début et de fin, et
retourner au format JSON les données de consommation en Watts entre ces
deux dates, demi-heure par demi-heure.

- Écrire un Dockerfile et un fichier docker-compose.yaml pour packager
l’application afin de pouvoir démarrer le projet avec la simple commande docker
compose up.

- Créer au moins un test du endpoint API

L’objectif est simplement de montrer une maîtrise minimale des technologies de base
de données relationnelles, des APIs, de la gestion d’erreur, du langage de
programmation python, de l’organisation de code. Afin de nous partager le code en
avance, vous pouvez créer une repo Github privé et y inviter @lovasoa, @tibz-enex et
@triskel78.

## Partie bonus

Si il vous reste du temps, vous pouvez implémenter au choix certains des points
bonus suivant:

- Déployer l’application et la base de données sur un cluster minikube local

- Implémenter le rafraîchissement automatique régulier des données depuis
RTE vers votre base de données.

N.B. : Ne faites les parties bonus que si vous êtes sûrs de ne plus pouvoir améliorer
votre solution pour l’exercice principal.

