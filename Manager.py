import sys
import os

  
def sauvegarder_liste(liste, nom_fichier):
    with open(nom_fichier, 'w') as file:
        for item in liste:
            file.write(f"{item}\n")
    print(f"Liste sauvegardée dans {nom_fichier}.")

def charger_liste(nom_fichier):
    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'r') as file:
            liste = [line.strip() for line in file]
        print(f"Liste chargée depuis {nom_fichier}.")
        return liste
    else:
        print(f"Aucun fichier trouvé avec le nom {nom_fichier}.")
        return []

def main():
    liste = []
    nom_fichier = "liste_de_courses.txt"

    # Charger la liste si le fichier existe
    liste = charger_liste(nom_fichier)

def main():
    liste = []
    nom_fichier = "liste_de_courses.txt"

    # Charger la liste si le fichier existe
    liste = charger_liste(nom_fichier)

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
        print(f"L'élément {Ajout} a bien été ajoutée")
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
        liste.remove(Ajout in liste)
        print("Votre liste a bien été effacée")
    elif userchoice == "5":
        exit = input("A bientot, êtes vous sur de quitter ?\n--->")
        if exit == "oui":
            sys.exit()
        elif exit == "non":
            userchoice == input(menu)
    elif userchoice == "6":
        sauvegarder_liste(liste, "nom_fichier")
    elif userchoice == "7":
        charger_liste("nom_fichier")
        
            
    print("-" * 50)


if __name__ == "__main__":
    main()   
    
