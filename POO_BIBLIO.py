class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.emprunts = {}

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def emprunter_livre(self, titre, emprunteur):
        for livre in self.livres:
            if livre.titre == titre and livre.disponible:
                livre.disponible = False
                self.emprunts[titre] = emprunteur
                print(f"{titre} a été emprunté par {emprunteur}.")
                return
        print(f"{titre} n'est pas disponible.")

    def rendre_livre(self, titre):
        if titre in self.emprunts:
            for livre in self.livres:
                if livre.titre == titre:
                    livre.disponible = True
                    del self.emprunts[titre]
                    print(f"{titre} a été rendu.")
                    return
        print(f"{titre} n'a pas été emprunté.")

    def afficher_disponibles(self):
        print("Livres disponibles :")
        for livre in self.livres:
            if livre.disponible:
                print(f"- {livre.titre} par {livre.auteur}")

    def rechercher_par_titre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                print(f"{livre.titre} par {livre.auteur}, année {livre.annee}")
                return
        print(f"Aucun livre trouvé avec le titre '{titre}'.")

    def rechercher_par_auteur(self, auteur):
        for livre in self.livres:
            if livre.auteur.lower() == auteur.lower():
                print(f"{livre.titre} par {livre.auteur}, année {livre.annee}")
        print(f"Aucun livre trouvé de l'auteur '{auteur}'.")

# Exemple d'utilisation
if __name__ == "__main__":
    livre1 = Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", 1997)
    livre2 = Livre("Le Seigneur des anneaux", "J.R.R. Tolkien", 1954)
    
    biblio = Bibliotheque()
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    
    
    biblio.emprunter_livre("Harry Potter à l'école des sorciers", "Alice")
    biblio.emprunter_livre("Le Seigneur des anneaux", "Bob")
    
    biblio.rendre_livre("Harry Potter à l'école des sorciers")
    
    biblio.afficher_disponibles()
    
    biblio.rechercher_par_titre("Le Seigneur des anneaux")
    biblio.rechercher_par_auteur("J.K. Rowling")
