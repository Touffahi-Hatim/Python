class Employe:
    def __init__(self, id: int, prenom: str, nom: str, age: int) -> None:
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.salaire = 0.0
        self.anciennete = 0  # Correction orthographique "onciente" -> "anciennete"

    def get_profil(self) -> str:
        full_profil = f"ID : {self.id}\n{self.nom} {self.prenom}\n{self.age} ans"
        return full_profil.title()

    def get_anciennete(self) -> None:
        print(f"L'employé avec l'ID {self.id} a {self.anciennete} jours d'ancienneté.")

    def get_salaire(self) -> None:
        print(f"Le salaire actuel de l'employé est : {self.salaire} dh")

    def update_anciennete(self, duree_passee: int) -> None:
        if duree_passee >= self.anciennete:
            self.anciennete = duree_passee
        else:
            print("Durée invalide. Veuillez réessayer.")

    def update_salaire(self, salaire_negocie: float) -> None:
        if salaire_negocie >= self.salaire and self.anciennete <= 30:
            self.salaire = salaire_negocie
        else:
            print("Salaire négocié invalide ou ancienneté trop élevée. Veuillez réessayer.")

    def increment_anciennete(self, jours: int) -> None:
        self.anciennete += jours

    def increment_salaire(self, montant_ajoute: float) -> None:
        self.salaire += montant_ajoute

# Exemple d'utilisation
employe1 = Employe(1, "Hatim", "Touffahi", 19)

print(employe1.get_profil())
employe1.get_anciennete()
employe1.get_salaire()
print("-----------------------")

employe1.update_anciennete(int(input("Entrez la durée passée dans l'entreprise (en jours) : ")))
employe1.update_salaire(float(input("Entrez le salaire négocié en dh : ")))
employe1.get_anciennete()
employe1.get_salaire()
print("-----------------------")

employe1.increment_anciennete(int(input("Entrez le nombre de jours à ajouter : ")))
employe1.increment_salaire(float(input("Entrez le montant à ajouter au salaire : ")))
employe1.get_anciennete()
employe1.get_salaire()
print("-----------------------")
