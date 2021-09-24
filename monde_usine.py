# -*- coding: utf-8 -*-
from monde_chromatique import MondeChromatique
from monde_simple import MondeSimple
from monde_simple_borne import MondeSimpleBorne

class MondeUsine:
    "Classe implémentant le pattern Factory pour la création et le chargement des mondes"

    @staticmethod    
    def charger(nomfichier):
        monde_class = ""
        monde_version = ""
        with open(nomfichier, "r") as file:
            # On recherche uniquement les deux propriétés permettant de déterminer
            # la classe à utiliser pour le chargement du monde.
            while (line := file.readline().rstrip()) and (not monde_class or not monde_version):
                if "monde.class" in line:
                    monde_class = line.replace("monde.class=", "").strip()
                elif "monde.version" in line:
                    monde_version = line.replace("monde.version=", "").strip()
            
            if not monde_class or not monde_version:
                raise SyntaxError("Le fichier de données est corrompu.")

            # Fermeture du fichier
            file.close()
        
        if monde_class == "MondeSimple" and monde_version =="1.0":
            monde = MondeSimple()
            monde.charger(nomfichier)
        elif monde_class == "MondeSimpleBorne" and monde_version =="1.0":
            monde = MondeSimpleBorne()
            monde.charger(nomfichier)
        elif monde_class == "MondeChromatique" and monde_version =="1.0":
            monde = MondeChromatique()
            monde.charger(nomfichier)
        else:
            raise NotImplementedError("La version du fichier de données n'est pas prise en charge par ce programme.")
        
        return monde
