# -*- coding: utf-8 -*-
"""
@author: Cédric Berteletti
Point d'entrée pour le programme du jeu de la vie
"""

import pygame
import math

# Constantes
LARGEUR_ECRAN = 900
HAUTEUR_ECRAN = 600


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

    # Boucle principale du jeu
    while danslejeu:
        # Récupération des événements du joueur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("On quitte")
                danslejeu = False

        #TODO
        print("TODO")

        # 60 images / seconde
        clock.tick(60)


print("Programme principal")
if __name__ == "__main__":
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass