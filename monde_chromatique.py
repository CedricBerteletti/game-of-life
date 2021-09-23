# -*- coding: utf-8 -*-
import pygame
import random
from monde_simple import MondeSimple

class MondeChromatique(MondeSimple):
    "Classe pour afficher et faire évoluer une version du jeu de la vie avec des cellules possédant"
    "des allèles de couleurs et pouvant muter"
    "Monde toroïdal"

    _NB_BITS_COULEURS = 4
    _TAUX_MUTATION = 1.0 / 100.0

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
        "Crée un nouvelle cellule, compatible avec le type du monde choisi, dans le contexte des coordonnées fournies (mais n'insère pas la cellule dans le monde)"
        voisins = self.voisins(colonne, ligne)
        rouges = []
        verts = []
        bleus = []
        for voisin in voisins:
            rouges.append(voisin[0])
            verts.append(voisin[1])
            bleus.append(voisin[2])
        rouge = self._valeur_allele(rouges)
        vert = self._valeur_allele(verts)
        bleu = self._valeur_allele(bleus)
        return (rouge, vert, bleu)

    def _couleur_cellule(self, colonne, ligne):        
        if self.cases[colonne][ligne] is not None:
            return self.cases[colonne][ligne]
        else:
            return (0, 0, 0)
    
    def _valeur_allele(self, valeurs):
        mutation  = random.uniform(0, 1.0)
        allele = 0
        if mutation <= self._TAUX_MUTATION:
            allele = random.randint(1, self._NB_BITS_COULEURS)*256/self._NB_BITS_COULEURS - 1
        else:
            allele = random.choice(valeurs)
        return allele
    