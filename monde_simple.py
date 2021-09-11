# -*- coding: utf-8 -*-
import pygame
import random

class MondeSimple:
    "Classe pour afficher et faire évoluer une version simple du jeu de la vie"
    "Monde toroïdal (haut du monde lié au bas, gauche du mon lié à la droite"

    def __init__(self, nb_colonnes=10, nb_lignes=10, taille_case=10):
        self.nb_colonnes = nb_colonnes
        self.nb_lignes = nb_lignes
        self.taille_case = taille_case
        self.init_cases(False)
    
    def init_cases(self, aleatoire):
        "Méthode pour initialiser le monde"
        self.cases = self._init_cases(aleatoire)
    
    def _init_cases(self, aleatoire):
        "Méthode retournant un tableau en 2D avec les cases initialisées"
        cases_vides = []
        for x in range (0, self.nb_colonnes):
            nouvelle_colonne = []
            for y in range (0, self.nb_lignes):
                nouvelle_colonne.append(self._init_value(aleatoire))
            cases_vides.append(nouvelle_colonne)
        return cases_vides

    def _init_value(self, aleatoire):
        "Méthode retournant la valeur d'initialisation à utiliser (méthode à surcharger dans d'autres types de monde)"
        if aleatoire:
            return bool(random.getrandbits(1))
        else:
            return False

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
        nouvelles_cases = self._init_cases(False)
        
        for y in range (0, self.nb_lignes):
            for x in range (0, self.nb_colonnes):
                nb_vois = self.nb_voisins(x, y)
                if nb_vois == 3:
                    nouvelles_cases[x][y] = True
                elif nb_vois == 2:
                    nouvelles_cases[x][y] = self.cases[x][y]
                else:
                    nouvelles_cases[x][y] = False

        self.cases = nouvelles_cases
    
    def nb_voisins(self, colonne, ligne):
        nb = 0

        c = self.cas_limite_col(colonne-1)
        l = self.cas_limite_ligne(ligne-1)
        if self.cases[c][l]:
            nb = nb+1
    
        c = self.cas_limite_col(colonne-1)
        l = self.cas_limite_ligne(ligne)
        if self.cases[c][l]:
            nb = nb +1

        c = self.cas_limite_col(colonne-1)
        l = self.cas_limite_ligne(ligne+1)
        if self.cases[c][l]:
            nb = nb +1

        c = self.cas_limite_col(colonne)
        l = self.cas_limite_ligne(ligne-1)
        if self.cases[c][l]:
            nb = nb +1

        c = self.cas_limite_col(colonne)
        l = self.cas_limite_ligne(ligne+1)
        if self.cases[c][l]:
            nb = nb +1

        c = self.cas_limite_col(colonne+1)
        l = self.cas_limite_ligne(ligne-1)
        if self.cases[c][l]:
            nb = nb +1

        c = self.cas_limite_col(colonne+1)
        l = self.cas_limite_ligne(ligne)
        if self.cases[c][l]:
            nb = nb +1

        c = self.cas_limite_col(colonne+1)
        l = self.cas_limite_ligne(ligne+1)
        if self.cases[c][l]:
            nb = nb +1
        
        return nb

    def cas_limite_col(self, col):
        "Gère les cas des bords pour les colonnes"
        if col < 0:
            return col + self.nb_colonnes
        elif col >= self.nb_colonnes:
            return col - self.nb_colonnes
        else:
            return col
    
    def cas_limite_ligne(self, ligne):
        "Gère les cas des bords pour les lignes"
        if ligne < 0:
            return ligne + self.nb_lignes
        elif ligne >= self.nb_lignes:
            return ligne - self.nb_lignes
        else:
            return ligne

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
            try:
                # Récupération des informations générales sur le monde
                raw_data = False
                while not raw_data and (line := file.readline().rstrip()):
                    if "monde.colonnes.nb" in line:
                        self.nb_colonnes = int(line.replace("monde.colonnes.nb=", "").strip())
                    elif "monde.lignes.nb" in line:
                        self.nb_lignes = int(line.replace("monde.lignes.nb=", "").strip())
                    elif "monde.case.taille" in line:
                        self.taille_case = int(line.replace("monde.case.taille=", "").strip())
                    raw_data = "[raw_data]" in line
                
                # Initialisation du monde vide
                self.cases = self._init_cases(False)

                # Récupération des données des cases
                for y in range (0, self.nb_lignes):
                    line = file.readline().rstrip()
                    for x in range (0, self.nb_colonnes):
                        if line[x] == "1":
                            self.cases[x][y] = True
            except Exception as error:
                raise SyntaxError("Le fichier de données est corrompu.")
            
            # Fermeture du fichier
            file.close()

