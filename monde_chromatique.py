# -*- coding: utf-8 -*-
import pygame
import random
from monde_simple import MondeSimple

class MondeChromatique(MondeSimple):
    "Classe pour afficher et faire évoluer une version du jeu de la vie avec des cellules possédant"
    "des gènes de couleurs RVB (avec différentes allèles pour la luminosité) et pouvant muter"
    "Monde toroïdal"

    _NB_NIVEAUX_LUMINOSITE_PAR_ALLELE = 4
    _TAUX_MUTATION = 1.0 / 100.0

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
            valeur = (255, 255, 255)
        return valeur

    def _couleur_cellule(self, colonne, ligne):
        "Couleur de remplissage de la cellule aux coordonnées indiquées"
        if self.cases[colonne][ligne] is not None:
            return self.cases[colonne][ligne]
        else:
            return (0, 0, 0)
    
    def _nouvelle_cellule(self, colonne, ligne):
        "Crée un nouvelle cellule, compatible avec le type du monde choisi, dans le contexte des coordonnées fournies (mais n'insère pas la cellule dans le monde)"
        "Pour ce monde chromatique, apparie les allèles des cellules voisines (en général, 3, avec la règle classique) pour les 3 gènes RVB"
        voisins = self.voisins(colonne, ligne)
        rouges = []
        verts = []
        bleus = []
        for voisin in voisins:
            rouges.append(voisin[0])
            verts.append(voisin[1])
            bleus.append(voisin[2])
        rouge = self._choisir_allele(rouges)
        vert = self._choisir_allele(verts)
        bleu = self._choisir_allele(bleus)
        return (rouge, vert, bleu)
    
    def _choisir_allele(self, alleles):
        "Renvoie l'une des allèles présentes dans les valeurs/allèles possibles, ou bien une nouvelle mutation"
        mutation  = random.uniform(0, 1.0)
        allele = 0
        if mutation <= self._TAUX_MUTATION:
            allele = int(random.randint(1, self._NB_NIVEAUX_LUMINOSITE_PAR_ALLELE)*256/self._NB_NIVEAUX_LUMINOSITE_PAR_ALLELE - 1)            
        else:
            allele = random.choice(alleles)
        return allele

    def _ecrire_case(self, fichier, case):
        if case:
            fichier.write(chr(case[0])+chr(case[1])+chr(case[2]))
        else:
            fichier.write(chr(0)+chr(0)+chr(0))

    def _lire_case_suivante(self, ligne_donnees):
        rouge = ord(ligne_donnees[0])
        vert = ord(ligne_donnees[1])
        bleu = ord(ligne_donnees[2])
        if rouge != 0 or vert != 0 or bleu != 0:
            return (rouge, vert, bleu), ligne_donnees[3:]
        else:
            return None, ligne_donnees[3:]
    