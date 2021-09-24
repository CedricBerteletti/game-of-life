# -*- coding: utf-8 -*-
import pygame
import random
from monde_abstrait import MondeAbstrait

class MondeSimple(MondeAbstrait):
    "Classe pour afficher et faire évoluer une version simple du jeu de la vie"
    "Monde toroïdal (haut du monde lié au bas, gauche du mon lié à la droite)"

    def __init__(self, nb_colonnes=10, nb_lignes=10, taille_case=10, dessiner_grille=True):
        self.nb_colonnes = nb_colonnes
        self.nb_lignes = nb_lignes
        self.taille_case = taille_case
        self.dessiner_grille = dessiner_grille
        self.init_cases(False)

    def _nouvelle_valeur_case(self, aleatoire):
        "Méthode retournant la valeur d'initialisation à utiliser"
        valeur = None
        if aleatoire and bool(random.getrandbits(1)):
            valeur = True 
        return valeur
    
    def _couleur_cellule(self, colonne, ligne):
        "Couleur de remplissage de la cellule aux coordonnées indiquées"
        if self.cases[colonne][ligne] is not None and self.cases[colonne][ligne]:
            couleur = (255, 255, 255)
        else:
            couleur = (0, 0, 0)
        return couleur
    
    def _nouvelle_cellule(self, colonne, ligne):
        "Crée un nouvelle cellule, compatible avec le type du monde choisi, dans le contexte des coordonnées fournies (mais n'insère pas la cellule dans le monde)"
        return True

    def enregistrer(self, nomfichier):
        with open(nomfichier, "w") as file:
            file.write("[configuration]\n")
            file.write("monde.class=" + self.__class__.__name__ + "\n")
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
                self.cases = self._nouvelles_cases(False)

                # Récupération des données des cases
                for y in range (0, self.nb_lignes):
                    line = file.readline().rstrip()
                    for x in range (0, self.nb_colonnes):
                        if line[x] == "1":
                            self.cases[x][y] = True
            except Exception as error:
                raise SyntaxError("Le fichier de données est corrompu.") from error
            
            # Fermeture du fichier
            file.close()

