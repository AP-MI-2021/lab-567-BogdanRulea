
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

    lista = []
    lista.append(("id", ID))
    lista.append(("nume", nume))
    lista.append(("descriere", descriere))
    lista.append(("PretAchizitie", float(pret_achizitie)))
    lista.append(("locatie", locatie))
    return lista

def getId(obiect):
    return obiect[0][1]

def getNume(obiect):
 
    return obiect[1][1]

def getDescriere(obiect):
    return obiect[2][1]

def getPretAchizitie(obiect):
    return obiect[3][1]

def getLocatie(obiect):
    return obiect[4][1]

def toString(obiect):
    return "ID: {}, Nume: {}, Descriere: {}, PretAchizitie: {}, Locatie: {}".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPretAchizitie(obiect),
        getLocatie(obiect)
    )

