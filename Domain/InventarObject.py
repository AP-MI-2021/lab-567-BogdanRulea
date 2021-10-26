def CreazaObiect(ID, nume, descriere, pret_achizitie, locatie):
    """Creare obiect

    Args:
        ID (integer): numar inventar
        nume (string): nume obiect
        descriere (string): descriere obiect
        pret_achizitie (float): pret achizitie
        locatie (4 chars): locatie
    
    Return: un dictionar cu specificatiile obiectului
    """
    return {
        "id" : ID,
        "nume" : nume,
        "descriere" : descriere,
        "PretAchizitie" : pret_achizitie,
        "locatie" : locatie
    }

def getId(obiect):
    return obiect["id"]

def getNume(obiect):
 
    return obiect["nume"]

def getDescriere(obiect):
    return obiect["descriere"]

def getPretAchizitie(obiect):
    return obiect["PretAchizitie"]

def getLocatie(obiect):
    return obiect["locatie"]

def toString(obiect):
    return "ID: {}, Nume: {}, Descriere: {}, PretAchizitie: {}, Locatie: {}".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPretAchizitie(obiect),
        getLocatie(obiect)
    )




