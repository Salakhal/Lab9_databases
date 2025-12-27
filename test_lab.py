import subprocess
import sys
import os
import glob
import time

# --- CONFIGURATION ---
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "1234" 
TEST_DB_NAME = "universite_test"

def run_command(command, description):
    print(f"\n--- {description} ---")
    try:
        # On utilise sys.executable pour utiliser le même python que celui en cours
        if command[0] == "python":
            command[0] = sys.executable
        
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(f" Succès.")
        if result.stdout:
            print(f"Sortie :\n{result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f" Erreur lors de l'exécution : {e}")
        print(f"Détails : {e.stderr}")
        sys.exit(1)

def main():
    print(" DÉMARRAGE DU SCRIPT DE TEST AUTOMATISÉ")

    # 1. Initialisation de la base principale (via models.py)
    run_command(["python", "models.py"], "Initialisation des tables (models.py)")

    # 2. Test du CLI : Ajout de cours
    run_command(
        ["python", "cli.py", "add-course", "Architecture des Ordinateurs", "--credits", "4"],
        "Test CLI : Ajout cours 1"
    )
    run_command(
        ["python", "cli.py", "add-course", "Cloud Computing", "--credits", "3"],
        "Test CLI : Ajout cours 2"
    )

    # 3. Test du CLI : Listage
    run_command(["python", "cli.py", "list-courses"], "Test CLI : Liste des cours")

    # 4. Test du Backup
    run_command(["python", "backup.py"], "Test du script de Backup")

    # 5. Restauration dans une base de test
    print("\n--- Restauration du dump dans une base de test ---")
    
    # Trouver le fichier dump le plus récent
    list_of_files = glob.glob('dump_universite_*.sql')
    if not list_of_files:
        print(" Erreur : Aucun fichier dump trouvé !")
        sys.exit(1)
    latest_dump = max(list_of_files, key=os.path.getctime)
    print(f" Fichier dump trouvé : {latest_dump}")

    # Création de la base de test et restauration
    # Note : On passe le mot de passe directement (attention en prod, mais OK pour un lab)
    mysql_cmd = [
        "mysql", 
        "-u", DB_USER, 
        f"-p{DB_PASS}", 
        "-e", f"DROP DATABASE IF EXISTS {TEST_DB_NAME}; CREATE DATABASE {TEST_DB_NAME}; USE {TEST_DB_NAME}; SOURCE {latest_dump};"
    ]
    
    try:
        subprocess.run(mysql_cmd, check=True)
        print(f" Restauration réussie dans la base '{TEST_DB_NAME}'.")
    except subprocess.CalledProcessError:
        print(" Erreur lors de la restauration MySQL via ligne de commande.")
        print("Assurez-vous que 'mysql' est bien dans votre PATH système.")
        sys.exit(1)

    print("\n TEST COMPLET TERMINÉ AVEC SUCCÈS !")

if __name__ == "__main__":
    main()
