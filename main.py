# -*- coding: utf-8 -*-
"""
@author: Cédric Berteletti
Point d'entrée pour le programme du jeu de la vie
"""

from monde_simple import MondeSimple
import pygame
from math import trunc

# Constantes
LARGEUR_ECRAN = 900
HAUTEUR_ECRAN = 600
TAILLE_CASE = 100
LARGEUR_GRILLE = trunc(LARGEUR_ECRAN / TAILLE_CASE)
HAUTEUR_GRILLE = trunc(HAUTEUR_ECRAN / TAILLE_CASE)


def main(args):
    print("Entrée dans la fonction main")

    # Initialisation de la fenêtre d'affichage
    pygame.init()
    ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
    pygame.display.set_caption("Jeu de la vie")

    # Autres initialiations
    # Timer
    clock = pygame.time.Clock()
    # Boucle d'évènements
    danslejeu = True
    # Initialisation du monde
    monde = MondeSimple(LARGEUR_GRILLE, HAUTEUR_GRILLE, TAILLE_CASE)
    monde.print()

    # Boucle principale du jeu
    while danslejeu:
        # Récupération des événements du joueur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("On quitte")
                danslejeu = False

        # monde.dessiner(ecran)

        # 60 images / seconde
        clock.tick(60)


print("Programme principal")
if __name__ == "__main__":
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass