import random

paquet_joueur1 = []
paquet_joueur2 = []

cartes = []
symboles_possibles = ["carreau", "pique", "trefle", "coeur"]

class Carte:
	def __init__(self, symbole: str, valeur: int):
		self.symbole = symbole
		self.valeur = valeur

	def __repr__(self):
		return f"{self.valeur} {self.symbole}"

	def comparer(self, deuxieme):
		if self.valeur > deuxieme.valeur:
			return "gagné"


class Paquet: 


	def set(self, symboles_possibles, cartes):
		for i in range(len(symboles_possibles)):
			for v in range(2, 15):
				temporaire = Carte(symboles_possibles[i], v)
				cartes.append(temporaire)
		random.shuffle(cartes)
		return cartes

	def distribuer(self, paquet_joueur1, paquet_joueur2, cartes):
		if cartes == []:
			return paquet_joueur1, paquet_joueur2
		else:
			paquet_joueur1.append(cartes[0])
			cartes.remove(cartes[0])
			paquet_joueur2.append(cartes[0])
			cartes.remove(cartes[0])
			return distribuer(self, paquet_joueur1, paquet_joueur, cartes)



paquet = Paquet()
print(paquet.set(symboles_possibles, cartes))
paquet.distribuer(paquet_joueur1, paquet_joueur2, cartes)


