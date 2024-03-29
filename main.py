# -*- coding: utf-8 -*-
"""
@author: Cédric Berteletti
Point d'entrée pour le programme du jeu de la vie
"""

from monde_simple import MondeSimple
from monde_usine import MondeUsine
import pygame
from math import trunc

# Constantes
LARGEUR_ECRAN = 900
HAUTEUR_ECRAN = 600
TAILLE_CASE = 10
NB_COLONNES = trunc(LARGEUR_ECRAN / TAILLE_CASE)
NB_LIGNES = trunc(HAUTEUR_ECRAN / TAILLE_CASE)

def ecrire_texte(surface, font, texte, x, y, couleur):
    texte_surface = font.render(texte, False, couleur, (100, 100, 100))
    return texte_surface

def main(args):
    print("Entrée dans la fonction main")

    # Initialisation de pygame et de la fenêtre d'affichage
    pygame.init()
    fenetre = (LARGEUR_ECRAN+1, HAUTEUR_ECRAN+1)
    ecran = pygame.display.set_mode(fenetre)
    pygame.display.set_caption("Jeu de la vie")
    ips = 2 # images par seconde
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 14)
    # Timer
    clock = pygame.time.Clock()

    # Autres initialiations
    # Boucle d'évènements
    danslejeu = True
    # Initialisation du monde
    monde = MondeSimple(NB_COLONNES, NB_LIGNES, TAILLE_CASE)
    # Fichier de sauvegarde du monde
    nom_fichier = "monde_par_default.vie"
    # Monde en pause ou en évolution 
    en_pause = True
    # Afficher l'aide
    aide = True
    # Afficher les infos
    infos = False
    # Pas d'évolution
    pas = 0

    # Boucle principale du jeu
    while danslejeu:
        # Récupération des événements du joueur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("On quitte")
                danslejeu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_MINUS and ips>1:
                    ips -= 1
                elif event.key == pygame.K_KP_PLUS:
                    ips += 1
                elif event.key == pygame.K_e:
                    monde.enregistrer(nom_fichier)
                elif event.key == pygame.K_c:
                    monde = MondeUsine.charger(nom_fichier)
                    pas = 0
                elif event.key == pygame.K_SPACE:
                    en_pause = not en_pause
                elif event.key == pygame.K_h:
                    aide = not aide
                elif event.key == pygame.K_i:
                    infos = not infos
                elif event.key == pygame.K_a:
                    monde.init_cases(True)
                    pas = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                case_ligne = int(y / TAILLE_CASE)
                case_colonne = int(x / TAILLE_CASE)
                monde.cases[case_colonne][case_ligne] = True

        # Initialisation de la nouvelle image
        surface_de_dessin = pygame.Surface(fenetre)

        # Rendu du nouvel état du monde
        if not en_pause:
            monde.evolution()
            pas += 1
        monde.dessiner(surface_de_dessin)

        # Bascule de la nouvelle image sur l'écran
        ecran.blit(surface_de_dessin, (0,0))
        if infos or aide:
            x_text = 0
            y_text = 0
            text_largeur, text_hauteur = font.size("txt")
            if infos:
                rouge = (0, 0, 200)
                texte_surface = ecrire_texte(ecran, font, "Vitesse : " + str(ips), x_text, y_text, rouge)   
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur
                texte_surface = ecrire_texte(ecran, font, "Pas d'évolution : " + str(pas), x_text, y_text, rouge)
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur
            if aide:
                vert = (0, 200, 0)
                texte_surface = ecrire_texte(ecran, font, "Touches :", x_text, y_text, vert)
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur
                texte_surface = ecrire_texte(ecran, font, "i : affiche les informations sur la simulation", x_text, y_text, vert)
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur
                texte_surface = ecrire_texte(ecran, font, "+ : augmente la vitesse de la simulation", x_text, y_text, vert)
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur
                texte_surface = ecrire_texte(ecran, font, "- : diminue la vitesse de la simulation", x_text, y_text, vert)
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur
                texte_surface = ecrire_texte(ecran, font, "Barre d'espace : pause/reprise", x_text, y_text, vert)
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur
                texte_surface = ecrire_texte(ecran, font, "a : réinitialiser le monde avec des valeurs aléatoires", x_text, y_text, vert)
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur
                texte_surface = ecrire_texte(ecran, font, "e : enregistrer le monde dans un fichier .vie", x_text, y_text, vert)
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur
                texte_surface = ecrire_texte(ecran, font, "c : charger le monde depuis un fichier .vie", x_text, y_text, vert)
                ecran.blit(texte_surface, (x_text, y_text))
                y_text += text_hauteur

        pygame.display.flip()

        # images / seconde
        clock.tick(ips)

    pygame.quit()


print("Programme principal")
if __name__ == "__main__":
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
