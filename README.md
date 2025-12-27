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

## Capture d’écran :
Voici un exemple de l'exécution du programme (screenshot) :

<img width="901" height="1346" alt="image" src="https://github.com/user-attachments/assets/7363b6ab-ca39-41b2-be14-7b0e103a9709" />

---

<img width="1122" height="785" alt="image" src="https://github.com/user-attachments/assets/fe0e5fab-f5f6-46da-9326-5b81fbb7378f" />

---

<img width="823" height="753" alt="image" src="https://github.com/user-attachments/assets/53518e7a-2eba-455e-8d21-38a6cb999d4a" />

---

<img width="817" height="697" alt="image" src="https://github.com/user-attachments/assets/73370301-cb08-4702-bb3c-d5f31d875d84" />


