
import pygame

class MondeSimple:
    "Classe pour afficher et faire évoluer une version simple du jeu de la vie"

    def __init__(self, nb_colonnes=10, nb_lignes=10, taille_case=10):
        self.nb_colonnes = nb_colonnes
        self.nb_lignes = nb_lignes
        self.taille_case = taille_case
        self.cases = self.init_cases()
    
    def init_cases(self):
        #print("init_cases")
        cases_vides = []
        for x in range (0, self.nb_colonnes):
            nouvelle_colonne = []
            for y in range (0, self.nb_lignes):
                nouvelle_colonne.append(False)
            cases_vides.append(nouvelle_colonne)
        return cases_vides

    def print(self):
        for y in range (0, self.nb_lignes):
            for x in range (0, self.nb_colonnes):
                print(self.cases[x][y], end=" ")
            print("")

    def dessiner(self, surface):
        couleur=(255, 255, 255)

        # Tracé des horizontales
        for y in range (0, self.nb_lignes+1):
            pygame.draw.line(surface, couleur, (0, y*self.taille_case),
                (self.nb_colonnes*self.taille_case, y*self.taille_case))

        # tracé des verticales
        for x in range (0, self.nb_colonnes+1):
            pygame.draw.line(surface, couleur, (x*self.taille_case, 0),
                ( x*self.taille_case, self.nb_lignes*self.taille_case))
        
        # tracé des cellules
        for y in range (0, self.nb_lignes):
            for x in range (0, self.nb_colonnes):
                if self.cases[x][y] == True:
                    x1 = x*self.taille_case
                    y1 = y*self.taille_case
                    pygame.draw.rect(surface, couleur, (x1, y1, self.taille_case, self.taille_case))

    def evolution(self):
        #print("evolution")
        nouvelles_cases = self.init_cases()
        
        for y in range (0, self.nb_lignes):
            for x in range (0, self.nb_colonnes):
                #nouvelles_cases[x][y] = self.cases[x][y]
                nouvelles_cases[x][y] = not self.cases[x][y]
        # TODO

        self.cases = nouvelles_cases

    def enregistrer(self, nomfichier):
        with open(nomfichier, "w") as file:
            file.write("[configuration]\n")
            file.write("monde.class=MondeSimple\n")
            file.write("monde.version=1.0\n")
            file.write("monde.colonnes.nb=" + str(self.nb_colonnes) + "\n")
            file.write("monde.lignes.nb=" + str(self.nb_lignes) + "\n")
            file.write("monde.case.taille=" + str(self.taille_case) + "\n")            
            file.write("[raw_data]\n")
            for y in range (0, self.nb_lignes):
                for x in range (0, self.nb_colonnes):
                    if self.cases[x][y]:
                        file.write("1")
                    else:
                        file.write("0")
                file.write("\n")
            file.close()

    def charger(self, nomfichier):
        with open(nomfichier, "r") as file:
            
            
            file.close()

