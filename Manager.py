import sys
import os

menu = """Bonjour! Bienvenue dans Manager 1.0!
Choissisez entre plusieurs options:
1- Ajouter un élément au manager
2- Enlever un élément du manager
3- Avoir un regard dessus
4- Réinitialiser votre liste
5- Quitter
6- Sauvegarder infos
7- Charger infos
Lequel choissisez-vous ?
--> """
liste = [""]
answer = ["1", "2", "3", "4", "5", "6", "7"]
chemin = "C/Users/Elimen/OneDrive/Documents"

while True:
    userchoice = ""
    while userchoice not in answer:
        userchoice = input(menu)
        if userchoice not in answer:
            print("Veuillez entrez une option valide")

    if userchoice == "1":
        Ajout = input("Que comptez vous ajouter ?\n-->")
        liste.append(Ajout)
        print("L'élément {liste} a bien été ajoutée")
    elif userchoice == "2" :
        Ajout = input("Quel élément comptez vous enlever ?\n-->")
        if Ajout in liste:
            liste.remove(Ajout)
            print(f"L'objet {Ajout} a bien été supprimé")
        else:
            print("Elément inexistant")
    elif userchoice == "3":
        if liste:
            print(f"Voici les éléments contenus dans votre liste: ")
            for i, Ajout in enumerate(liste):
                print(f"{i + 1}. {Ajout}")
        else:
            print("Votre liste dans le ne contient aucun élément")
    elif userchoice == "4":
        liste.remove()
        print("Votre liste a bien été effacée")
    elif userchoice == "5":
        exit = input("A bientot, êtes vous sur de quitter ?\n--->")
        if exit == "oui":
            sys.exit()
        elif exit == "non":
            userchoice == input(menu)
    elif userchoice == "6":
        dossier_save = os.path.join(chemin, "pysave")
        os.makedirs("pysave")
        if os.path.exists("pysave"):
            print("Votre dossier de sauvegarde a bien été créée UWU...")
            userchoice = input(menu)
        else:
            print("Charger votre sauvegarde python")
    elif userchoice == "7":
        os.path.join(chemin, "pygame")
        
            
    print("-" * 50)


    
    
