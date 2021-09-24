
import pygame
import random

class MondeAbstrait:
    "Classe abstraite pour gérer un monde du jeu de la vie"
    "Monde toroïdal par défaut (haut du monde lié au bas, gauche du mon lié à la droite)"

    # Propriétés abstraites des mondes
    nb_colonnes = 10
    nb_lignes = 10
    taille_case = 10
    dessiner_grille = True
    
    def init_cases(self, aleatoire):
        "Méthode pour initialiser le monde"
        self.cases = self._nouvelles_cases(aleatoire)
    
    def _nouvelles_cases(self, aleatoire):
        "Méthode retournant un tableau en 2D avec les cases initialisées"
        cases_vides = []
        for x in range (0, self.nb_colonnes):
            nouvelle_colonne = []
            for y in range (0, self.nb_lignes):
                nouvelle_colonne.append(self._nouvelle_valeur_case(aleatoire))
            cases_vides.append(nouvelle_colonne)
        return cases_vides

    def _nouvelle_valeur_case(self, aleatoire):
        "Méthode retournant la valeur d'initialisation à utiliser (méthode à surcharger dans d'autres types de monde)"
        raise NotImplementedError()

    def print(self):
        for y in range (0, self.nb_lignes):
            for x in range (0, self.nb_colonnes):
                print(self.cases[x][y], end=" ")
            print("")
        print("")

    def print_nb_voisins(self):
        for y in range (0, self.nb_lignes):
            for x in range (0, self.nb_colonnes):
                print(self.nb_voisins(x, y), end=" ")
            print("")
        print("")
    
    def case(self, colonne, ligne):
        "Récupère la cellule présente dans la case, en gérant les dépassements d'index dans un monde toroïdal"
        c = colonne
        l = ligne
        if colonne < 0:
            c = c + self.nb_colonnes
        if colonne >= self.nb_colonnes:
            c = c - self.nb_colonnes
        if ligne < 0:
            l = l + self.nb_lignes
        if ligne >= self.nb_lignes:
            l = l - self.nb_lignes
        return self.cases[c][l]

    def dessiner(self, surface):
        blanc = (128, 128, 128)
        if self.dessiner_grille:
            self._dessiner_grille(surface, blanc)
        self._dessiner_cellules(surface)    
    
    def _dessiner_grille(self, surface, couleur):
        # Tracé des horizontales
        for y in range (0, self.nb_lignes+1):
            pygame.draw.line(surface, couleur, (0, y*self.taille_case),
                (self.nb_colonnes*self.taille_case, y*self.taille_case))

        # tracé des verticales
        for x in range (0, self.nb_colonnes+1):
            pygame.draw.line(surface, couleur, (x*self.taille_case, 0),
                ( x*self.taille_case, self.nb_lignes*self.taille_case))
        
    def _dessiner_cellules(self, surface):
        # tracé des cellules
        for y in range (0, self.nb_lignes):
            for x in range (0, self.nb_colonnes):                
                x1 = x*self.taille_case
                y1 = y*self.taille_case
                if self.dessiner_grille:
                    epaisseur_grille = 1
                else:
                    epaisseur_grille = 0
                pygame.draw.rect(surface, self._couleur_cellule(x, y), (x1+epaisseur_grille, y1+epaisseur_grille,
                    self.taille_case-epaisseur_grille, self.taille_case-epaisseur_grille))
    
    def _couleur_cellule(self, colonne, ligne):
        "Couleur de remplissage de la cellule aux coordonnées indiquées"
        if self.cases[colonne][ligne] is not None:
            couleur = (255, 255, 255)
        else:
            couleur = (0, 0, 0)
        return couleur
    
    def evolution(self):
        "Règles d'évolution du monde"
        nouvelles_cases = self._nouvelles_cases(False)
        
        for y in range (0, self.nb_lignes):
            for x in range (0, self.nb_colonnes):
                nb_vois = self.nb_voisins(x, y)
                if nb_vois == 3:
                    nouvelles_cases[x][y] = self._nouvelle_cellule(x, y)
                elif nb_vois == 2:
                    nouvelles_cases[x][y] = self.cases[x][y]
                else:
                    nouvelles_cases[x][y] = None

        self.cases = nouvelles_cases

    def _nouvelle_cellule(self, colonne, ligne):
        "Crée un nouvelle cellule, compatible avec le type du monde choisi, dans le contexte des coordonnées fournies (mais ne l'insère pas dans le monde)"
        raise NotImplementedError()
    
    def nb_voisins(self, c, l):
        nb = 0

        if self.case(c-1, l-1) is not None:
            nb = nb+1

        if self.case(c-1, l) is not None:
            nb = nb+1
                
        if self.case(c-1, l+1) is not None:
            nb = nb+1
                
        if self.case(c, l-1) is not None:
            nb = nb+1
                
        if self.case(c, l+1) is not None:
            nb = nb+1
                
        if self.case(c+1, l-1) is not None:
            nb = nb+1
                
        if self.case(c+1, l) is not None:
            nb = nb+1
                
        if self.case(c+1, l+1) is not None:
            nb = nb+1
        
        return nb
    
    def voisins(self, c, l):
        voisins = []
        case = self.case(c-1, l-1)
        if case is not None:
            voisins.append(case)
        case = self.case(c-1, l)
        if case is not None:
            voisins.append(case)
        case = self.case(c-1, l+1)
        if case is not None:
            voisins.append(case)
        case = self.case(c, l-1)
        if case is not None:
            voisins.append(case)
        case = self.case(c, l+1)
        if case is not None:
            voisins.append(case)
        case = self.case(c+1, l-1)
        if case is not None:
            voisins.append(case)
        case = self.case(c+1, l)
        if case is not None:
            voisins.append(case)
        case = self.case(c+1, l+1)
        if case is not None:
            voisins.append(case)
        return voisins

    def enregistrer(self, nomfichier):
        raise NotImplementedError()

    def charger(self, nomfichier):
        raise NotImplementedError()