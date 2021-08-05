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
TAILLE_CASE = 10
NB_COLONNES = trunc(LARGEUR_ECRAN / TAILLE_CASE)
NB_LIGNES = trunc(HAUTEUR_ECRAN / TAILLE_CASE)


def main(args):
    print("Entrée dans la fonction main")

    # Initialisation de la fenêtre d'affichage
    pygame.init()
    fenetre = (LARGEUR_ECRAN+1, HAUTEUR_ECRAN+1)
    ecran = pygame.display.set_mode(fenetre)
    pygame.display.set_caption("Jeu de la vie")

    # Autres initialiations
    # Timer
    clock = pygame.time.Clock()
    # Boucle d'évènements
    danslejeu = True
    # Initialisation du monde
    monde = MondeSimple(NB_COLONNES, NB_LIGNES, TAILLE_CASE)
    #monde.print()

    # Boucle principale du jeu
    while danslejeu:
        # Récupération des événements du joueur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("On quitte")
                danslejeu = False

        # Initialisation de la nouvelle image
        surface_de_dessin = pygame.Surface(fenetre)

        # Rendu du nouvel état du monde
        monde.dessiner(surface_de_dessin)

        # Bascule de la nouvelle image sur l'écran
        ecran.blit(surface_de_dessin,(0,0))
        pygame.display.flip()

        # 60 images / seconde
        clock.tick(60)


    pygame.quit()


print("Programme principal")
if __name__ == "__main__":
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass