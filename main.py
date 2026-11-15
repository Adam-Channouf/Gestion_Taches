
taches = []

while True:
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Titre de la tâche : ").strip()

        if titre == "":
            print("Erreur : le titre ne peut pas être vide.")
        else:
            taches.append(titre)
            print("Tâche ajoutée avec succès.")

    elif choix == "2":
        if len(taches) == 0:
            print("Aucune tâche enregistrée.")
        else:
            print("\n=== LISTE DES TÂCHES ===")

            i = 0
            while i < len(taches):
                print(i + 1, "-", taches[i])
                i = i + 1

    
    elif choix == "3":
        mot_cle = input("Mot-clé à rechercher : ").strip()

        if mot_cle == "":
            print("Erreur : le mot-clé ne peut pas être vide.")
        else:
            trouve = False
            i = 0

            while i < len(taches):
                if mot_cle.lower() in taches[i].lower():
                    print("Tâche trouvée :")
                    print(i + 1, "-", taches[i])
                    trouve = True

                i = i + 1

            if trouve == False:
                print("Aucune tâche correspondante.")


    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Option invalide. Veuillez réessayer.")

