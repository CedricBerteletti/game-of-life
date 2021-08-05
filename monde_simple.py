
import pygame

class MondeSimple:
    "Classe pour afficher et faire évoluer une version simple du jeu de la vie"

    def __init__(self, nb_colonnes, nb_lignes, taille_case):
        self.nb_colonnes = nb_colonnes
        self.nb_lignes = nb_lignes
        self.taille_case = taille_case
        self.cases = []
        for x in range (0, self.nb_colonnes):
            nouvelle_colonne = []
            for y in range (0, self.nb_lignes):
                nouvelle_colonne.append(False)
            self.cases.append(nouvelle_colonne)    

    def print(self):
        for y in range (0, self.nb_lignes):
            for x in range (0, self.nb_colonnes):
                print(self.cases[x][y], end=" ")
            print("")

    def dessiner(self, surface):
        couleur=(255, 255, 255)

        # Tracé des horizontales
            # pygame.draw.line(surface, couleur, (0, 0),
            #     (self.nb_colonnes*self.taille_case, 0))
            # pygame.draw.line(surface, couleur, (0, self.taille_case),
            #     (self.nb_colonnes*self.taille_case, self.taille_case))
            # pygame.draw.line(surface, couleur, (0, 2*self.taille_case),
            #     (self.nb_colonnes*self.taille_case, 2*self.taille_case))
        for y in range (0, self.nb_lignes+1):
            pygame.draw.line(surface, couleur, (0, y*self.taille_case),
                (self.nb_colonnes*self.taille_case, y*self.taille_case))

        #pygame.draw.line(surface, couleur, (00, 100), ( 900, 100))
        #pygame.draw.line(surface, couleur, (00, 200), ( 900, 200))
        #pygame.draw.line(surface, couleur, (00, 300), ( 900, 300))
        #pygame.draw.line(surface, couleur, (00, 400), ( 900, 400))
        #pygame.draw.line(surface, couleur, (00, 500), ( 900, 500))
        #pygame.draw.line(surface, couleur, (100, 000), ( 100, 600))
        #pygame.draw.line(surface, couleur, (200, 000), ( 200, 600))
        #pygame.draw.line(surface, couleur, (300, 000), ( 300, 600))
        #pygame.draw.line(surface, couleur, (400, 000), ( 400, 600))
        #pygame.draw.line(surface, couleur, (500, 000), ( 500, 600))
        #pygame.draw.line(surface, couleur, (600, 000), ( 600, 600))
        #pygame.draw.line(surface, couleur, (700, 000), ( 700, 600))
        #pygame.draw.line(surface, couleur, (800, 000), ( 800, 600))
        #pygame.draw.line(surface, couleur, (900, 000), ( 900, 600))

        #tracer des verticales
        for x in range (0, self.nb_colonnes+1):
            pygame.draw.line(surface, couleur, (x*self.taille_case, 0),
                ( x*self.taille_case, self.nb_lignes*self.taille_case))
        







