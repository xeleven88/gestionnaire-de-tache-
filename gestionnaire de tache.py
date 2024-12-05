taches = []

def afficher_taches():
    """Affiche toutes les tâches."""
    if not taches:
        print("Aucune tâche pour le moment.")
    else:
        print("\nListe des tâches :")
        for i, (tache, terminee) in enumerate(taches, start=1):
            status = "✓" if terminee else "✗"
            print(f"{i}. {tache} [{status}]")



def ajouter_tache():
    nouvelle_tache = input("Entrez la description de la tâche : ")
    taches.append((nouvelle_tache, False))
    print(f"Tâche ajoutée : {nouvelle_tache}")



def terminer_tache():
    """Marque une tâche comme terminée."""
    afficher_taches()
    if taches:
        try:
            index = int(input("Entrez le numéro de la tâche à marquer comme terminée : ")) - 1
            if (index >= 0) and (index < len(taches)):
                tache, _ = taches[index]
                taches[index] = (tache, True)
                print(f"Tâche terminée : {tache}")
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")




def menu():
    """Affiche le menu principal."""
    while True:
        print("\n--- Gestionnaire de Tâches ---")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Terminer une tâche")
        print("4. Quitter")

        choix = input("Entrez votre choix : ")
        if choix == "1":
            afficher_taches()
        elif choix == "2":
            ajouter_tache()
        elif choix == "3":
            terminer_tache()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# test
menu()