
import pygame

class MondeSimple:
    "Classe pour afficher et faire évoluer une version simple du jeu de la vie"

    def __init__(self, largeur_grille, hauteur_grille, taille_case):
        self.largeur_grille = largeur_grille
        self.hauteur_grille = hauteur_grille
        self.taille_case = taille_case
        self.cases = []
        for x in range (0, self.largeur_grille):
            nouvelle_colonne = []
            for y in range (0, self.hauteur_grille):
                nouvelle_colonne.append(False)
            self.cases.append(nouvelle_colonne)    

    def print(self):
        for y in range (0, self.hauteur_grille):
            for x in range (0, self.largeur_grille):
                print(self.cases[x][y], end=" ")
            print("")

    def dessiner(self, surface):
        couleur=(255, 255, 255)
        pygame.draw.line(surface, couleur, (10, 10), (100, 300))





