# Lab 9 : Programmation avancée & Administration de Bases de Données

Ce projet est une réalisation pratique du Lab 9. Il démontre l'intégration entre **Python** et **MySQL** à travers plusieurs méthodes : connecteurs natifs, ORM (Object Relational Mapping) et automatisation de tâches d'administration.

## 📂 Structure du Projet

Voici la description des fichiers présents dans ce dépôt :

* **`db.py`** : Gestion de la connexion à la base de données utilisant un **pool de connexions** (MySQL Connector) pour optimiser les performances.
* **`models.py`** : Définition des modèles de données (Étudiant, Cours, Notes, etc.) via l'ORM **SQLAlchemy**. Exécuter ce fichier crée les tables dans la base.
* **`cli.py`** : Interface en ligne de commande (CLI) construite avec la librairie `click`. Elle permet d'ajouter et de lister des cours directement depuis le terminal.
* **`backup.py`** : Script d'automatisation qui exécute un **dump SQL** de la base de données (sauvegarde).
* **`universite_dump.sql`** : Fichier de sauvegarde généré par le script de backup.

## 🛠️ Prérequis

* Python 3.x
* Serveur MySQL local
* Bibliothèques Python : `mysql-connector-python`, `sqlalchemy`, `pymysql`, `click`


