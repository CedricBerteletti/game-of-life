# -*- coding: utf-8 -*-
import pygame
import random
from monde_simple import MondeSimple

class MondeChromatique(MondeSimple):
    "Classe pour afficher et faire évoluer une version du jeu de la vie avec des cellules possédant"
    "des allèles de couleurs et pouvant muter"
    "Monde toroïdal"

    def __init__(self, nb_colonnes=10, nb_lignes=10, taille_case=10):
        self.nb_colonnes = nb_colonnes
        self.nb_lignes = nb_lignes
        self.taille_case = taille_case
        self.init_cases(False)
    
    def _nouvelle_valeur_case(self, aleatoire):
        "Méthode retournant la valeur d'initialisation à utiliser"
        valeur = None
        if aleatoire and bool(random.getrandbits(1)):
            valeur = (255, 255, 255)
        return valeur
    
    def _nouvelle_cellule(self, colonne, ligne):
        return (255, 255, 255)

    def _couleur_cellule(self, colonne, ligne):        
        if self.cases[colonne][ligne] is not None:
            return self.cases[colonne][ligne]
        else:
            return (0, 0, 0)
    