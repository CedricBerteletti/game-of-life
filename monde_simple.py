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

    def _ecrire_case(self, fichier, case):
        if case:
            fichier.write("1")
        else:
            fichier.write("0")

    def _lire_case_suivante(self, ligne_donnees):
        valeur = ligne_donnees[0]
        if ligne_donnees[0] == "1":
            return True, ligne_donnees[1:]
        else:
            return None, ligne_donnees[1:]

