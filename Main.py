
import random


class Carte:
    def __init__(self, symbole: str, valeur: int):
        self.symbole = symbole
        self.valeur = valeur

    def __repr__(self):
        noms = {
            1: "As",
            11: "Valet",
            12: "Dame",
            13: "Roi"
        }
        return f"{noms.get(self.valeur, self.valeur)} {self.symbole}"

    def comparer(self, autre):
        if self > autre:
            return 1
        elif self < autre:
            return -1
        return 0

    def __eq__(self, autre):
        return self.valeur == autre.valeur

    def __gt__(self, autre):
        return self.valeur > autre.valeur

    def __lt__(self, autre):
        return self.valeur < autre.valeur


class Paquet:
    def __init__(self):
        self.cartes = []

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

    def recevoir(self, carte):
        self.cartes.append(carte)

    def tirer(self):
        if not self.cartes:
            return None
        return self.cartes.pop(0)

    def envoyer(self, destination):
        carte = self.tirer()
        if carte is not None:
            destination.recevoir(carte)

    def recuperer(self, source):
        while len(source) > 0:
            self.recevoir(source.tirer())

    def __len__(self):
        return len(self.cartes)


class Partie:
    def __init__(self, mainj1, mainj2):
        self.mainj1 = mainj1
        self.mainj2 = mainj2

        self.zone_bataille = Paquet()

        self.defausse1 = Paquet()
        self.defausse2 = Paquet()

    def preparer(self, main, defausse, nombre):
        if len(main) < nombre and len(defausse) > 0:
            defausse.melanger()
            main.recuperer(defausse)

        return len(main) >= nombre

    def jouer_bataille(self):
    
        self.mainj1.envoyer(self.zone_bataille)
        self.mainj2.envoyer(self.zone_bataille)
        while True:
            carte1 = self.zone_bataille.cartes[-2]
            carte2 = self.zone_bataille.cartes[-1]

            resultat = carte1.comparer(carte2)

            if resultat == 1:
                return self.defausse1

            elif resultat == -1:
                return self.defausse2

            else:
                pret1 = self.preparer(
                    self.mainj1, self.defausse1, 2
                )
                pret2 = self.preparer(
                    self.mainj2, self.defausse2, 2
                )

                if not pret1 and not pret2:
                    return None
                elif not pret1:
                    return self.defausse2
                elif not pret2:
                    return self.defausse1

                
                self.mainj1.envoyer(self.zone_bataille)
                self.mainj2.envoyer(self.zone_bataille)

                
                self.mainj1.envoyer(self.zone_bataille)
                self.mainj2.envoyer(self.zone_bataille)

    def jouer(self):
        while True:

            pret1 = self.preparer(
                self.mainj1, self.defausse1, 1
            )
            pret2 = self.preparer(
                self.mainj2, self.defausse2, 1
            )

            if not pret1 and not pret2:
                print("Match nul !")
                break
            elif not pret1:
                print("Le joueur 2 gagne !")
                break
            elif not pret2:
                print("Le joueur 1 gagne !")
                break

            gagnant = self.jouer_bataille()

            if gagnant is None:
                print("Match nul !")
                break

            gagnant.recuperer(self.zone_bataille)



# Prépaparation du jeu
paquet_initial = Paquet()
paquet_initial.remplir()
paquet_initial.melanger()

mainj1 = Paquet()
mainj2 = Paquet()

for i in range(26):
    mainj1.recevoir(paquet_initial.tirer())
    mainj2.recevoir(paquet_initial.tirer())

partie = Partie(mainj1, mainj2)
partie.jouer()
