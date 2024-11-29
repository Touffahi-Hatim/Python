class Omployes:
    def __init__(self, id:int, prenom, nom, age:int, ) -> None:
        self.id=id
        self.prenom=prenom
        self.nom=nom
        self.age=age
        self.salaire=0.0
        self.onciente=0
    def get_profil(self):
        full_profil=f"id :{self.id}\n{self.nom} {self.prenom}\n{self.age} years old"
        return full_profil.title()
    
    
    def get_Onciente(self):
        print(f"l'omploye de l'id {self.id} a {self.onciente}j d'onciente.")
    def get_salaire(self):
        print(f"le salaire actuel de l'omploye est :{self.salaire}dh")
    def update_Onciente(self, duree_passe):
        if  duree_passe>=self.onciente:
            self.onciente=duree_passe
        else :
            print("try again!")
    def ubdate_salaire(self, salaire_negocie):
        if salaire_negocie>=self.salaire and self.onciente<=30:
            self.salaire=salaire_negocie
        else:
            print("try again")
    def Increment_Onciente(self, jours):
        self.onciente+=jours

    def Increment_salaire(self, montant_ajoute):
        self.salaire+=montant_ajoute
        

O1=Omployes(1,"hatim","touffahi",19)

print(O1.get_profil())
O1.get_Onciente()
O1.get_salaire()
print("-----------------------")
O1.update_Onciente(int(input("entrer la duree passe dans l'entreprise :")))
O1.ubdate_salaire(float(input("entrer le salaire negocie en dh ici :")))
O1.get_Onciente()
O1.get_salaire()
print("-----------------------")
O1.Increment_Onciente(int(input("entrer les jours a ajoutes : ")))
O1.Increment_salaire(float(input(f"entrer le montant a ajoute :")))
O1.get_Onciente()
O1.get_salaire()





        