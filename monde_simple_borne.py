# -*- coding: utf-8 -*-
import pygame
import random
from monde_simple import MondeSimple

class MondeSimpleBorne(MondeSimple):
    "Classe pour afficher et faire évoluer une version simple du jeu de la vie"
    "Monde borné (pas de liaison haut/bas, gauche/droite)"

    def __init__(self, nb_colonnes=10, nb_lignes=10, taille_case=10):
        self.nb_colonnes = nb_colonnes
        self.nb_lignes = nb_lignes
        self.taille_case = taille_case
        self.init_cases(False)
    
    def case(self, colonne, ligne):
        "Récupère la cellule présente dans la case, en gérant les dépassements d'index dans un monde borné"
        if colonne >= 0 and colonne < self.nb_colonnes and ligne >= 0 and ligne < self.nb_lignes:
            return self.cases[colonne][ligne]
        else:
            return None