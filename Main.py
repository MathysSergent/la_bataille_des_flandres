import random

compteur1 = 0
compteur2 = 0

symboles_possibles = ["carreau", "pique", "trefle", "coeur"]

class Carte:
	def __init__(self, symbole: str, valeur: int):
		self.symbole = symbole
		self.valeur = valeur

	def __repr__(self):
		return f"{self.valeur} {self.symbole}"

	def __eq__(self, autre):
		return self.valeur == autre.valeur

	def __gt__(self, autre):
		return self.valeur > autre.valeur

	def __lt__(self, autre):
		return self.valeur < autre.valeur

	def __ge__(self, autre):
		return self.valeur >= autre.valeur

	def __le__(self, autre):
		return self.valeur <= autre.valeur


	def comparer(self, autre, compteur1, compteur2, mainj1, mainj2):
		if self > autre:
			mainj1.cartes.remove(mainj1[0])
			mainj2.cartes.remove(mainj2[0])
			compteur1 += 1
			return compteur1, compteur2
		elif self == autre:
			print("bataille!")
			mainj1.cartes.remove(mainj1[0, 1])
			mainj2.cartes.remove(mainj2[0, 1])
			mainj1[2].comparer(mainj2.cartes[1], compteur1, compteur2, mainj1, mainj2)

		elif self < autre:
			mainj1.cartes.remove(mainj1[0])
			mainj2.cartes.remove(mainj2[0])
			compteur2 += 1
			return compteur1, compteur2
		else:
			print("erreur")

			
class Paquet:
    def __init__(self):
        self.cartes = []

    def __getitem__(self, index):
        return self.cartes[index]

    def remplir(self):
        symboles = ["carreau", "pique", "trèfle", "cœur"]
        valeurs = range(1, 14)
        self.cartes = [
            Carte(symbole, valeur)
            for symbole in symboles
            for valeur in valeurs
        ]


    def melanger(self):
        random.shuffle(self.cartes)

    def tirer(self):
        if not self.cartes:
            return None
        return self.cartes.pop()

    def recevoir(self, carte):
    	self.cartes.append(carte)

    def __len__(self):
        return len(self.cartes)

def jouer(mainj1, mainj2, compteur1, compteur2):
	while mainj1 != [] and mainj2 != []:
		compteur1, compteur2 = mainj1[0].comparer(mainj2[0], compteur1, compteur2, mainj1, mainj2)
	return print("joueur 1 =", compteur1,"et joueur 2 =", compteur2)
		
paquet_initial = Paquet()
paquet_initial.remplir()
paquet_initial.melanger()

mainj1 = Paquet()
mainj2 = Paquet()

for i in range(26):
	mainj1.recevoir(paquet_initial.tirer())
	mainj2.recevoir(paquet_initial.tirer())

jouer(mainj1, mainj2, compteur1, compteur2)
