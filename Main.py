import random

main_joueur1 = []
main_joueur2 = []

compteur1 = 0
compteur2 = 0

cartes = []
symboles_possibles = ["carreau", "pique", "trefle", "coeur"]

class Carte:
	def __init__(self, symbole: str, valeur: int):
		self.symbole = symbole
		self.valeur = valeur

	def __repr__(self):
		return f"{self.valeur} {self.symbole}"

	def __eq__(self, autre):
		if self.valeur == autre.valeur:
			return True
		else:
			return False

	def __gt__(self, autre):
		if self.valeur >= autre.valeur:
			return True
		else:
			return False

	def __lt__(self, autre):
		if self.valeur <= autre.valeur:
			return True
		else: 
			return False


	def comparer(self, autre, compteur1, compteur2, main_joueur1, main_joueur2):
		if self > autre:
			main_joueur1.remove(main_joueur1[0])
			main_joueur2.remove(main_joueur2[0])
			compteur1 += 1
			print(compteur1)
			return compteur1, compteur2
		elif self < autre:
			main_joueur1.remove(main_joueur1[0])
			main_joueur2.remove(main_joueur2[0])
			compteur2 += 1
			return compteur1, compteur2
		""" BUG elif self == autre:
			print("bataille!")
			main_joueur1.remove(main_joueur1[0, 1])
			main_joueur2.remove(main_joueur2[0, 1])
			main_joueur1[2].comparer(main_joueur2[2], compteur1, compteur2, main_joueur1, main_joueur2)"""
		else:
			print("erreur")

			
class Paquet:
    def __init__(self):
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

    def __len__(self):
        return len(self.cartes)

def jouer(main_joueur1, main_joueur2, compteur1, compteur2):
	while main_joueur1 != [] and main_joueur2 != []:
		compteur1, compteur2 = main_joueur1[0].comparer(main_joueur2[0], compteur1, compteur2, main_joueur1, main_joueur2)
	return compteur1, compteur2
		
paquet = Paquet()
paquet.melanger()

main_joueur1 = [paquet.tirer() for i in range(26)]
main_joueur2 = [paquet.tirer() for i in range(26)]
print(main_joueur1, main_joueur2)

print(jouer(main_joueur1, main_joueur2, compteur1, compteur2))