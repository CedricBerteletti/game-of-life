from monde_simple import MondeSimple

class MondeUsine:
    "Classe implémentant le pattern Factory pour la création et le chargement des mondes"

    def charger(nomfichier):
        monde_class = ""
        monde_version = ""
        with open(nomfichier, "r") as file:
            while (line := file.readline().rstrip()) and (not monde_class or not monde_version):
                if "monde.class" in line:
                    monde_class = line.replace("monde.class=", "").strip()
                if "monde.version" in line:
                    monde_version = line.replace("monde.version=", "").strip()
            file.close()
        
        if monde_class == "MondeSimple" and monde_version =="1.0":
            monde = MondeSimple()
            monde.charger(nomfichier)
        
        return monde
        
    charger = staticmethod(charger)
