from Domain.InventarObject import CreazaObiect, getId

def AdaugaObiectLista(id, nume, descriere, pret_achizitie, locatie, lista):
    """Adauga un obiect intr-o lista data

    Args:
        id (integer): id obiect
        nume (string): nume obiect
        descriere (string): descriere obiect
        pret_achizitie (float): pret achizitie obiect
        locatie (4 chars): locatie obiect
        lista (list[int]): lista in care trebuie adaugat obiectul
    """
    rezultat = lista
    if GetById(id,lista) == None:
        ObiectNou = CreazaObiect(id, nume, descriere, pret_achizitie, locatie)
        return lista + [ObiectNou]
    else:
       raise ValueError("Deja exista un obiect cu ID-ul dat.")


def GetById(id, lista):
    """Returneaza obiectul cu id-ul dat din lista

    Args:
        id (integer): id obiect
        lista (list[int]): lista data
    """
    for obiect in lista:
        if getId(obiect) == id:
            return obiect
    
    return None


def StergereObiectLista(id, lista):
    """Sterge un obiect din lista data

    Args:
        id (integer): id obiect
        lista (list[int]): lista data
    """
    if GetById(id, lista) is None:
        raise ValueError("Obiectul cu ID-ul dat nu exista.")
        return None
    return [obiect for obiect in lista if getId(obiect) != id]


def ModificareObiectLista(id, nume, descriere, pret_achizitie, locatie, lista):
    """Modifica un obiect cu id-ul dat din lista

    Args:
        id (integer): id obiect
        nume (string): nume obiect
        descriere (string): descriere obiect
        pret_achizitie (float): pret achizitie obiect
        locatie (4 chars): locatie obiect
        lista (list[int]): lista in care trebuie adaugat obiectul

    Returns:
        lista[int]: lista optinuta in urma modificarii obiectului
    """
    listaNoua = []
    if GetById(id, lista) is None:
        raise ValueError("Obiectul cu ID-l dat nu exista.")
    for obiect in lista:
        if getId(obiect) == id:
            ObiectNou = CreazaObiect(id, nume, descriere, pret_achizitie, locatie)
            listaNoua.append(ObiectNou)
        else:
            listaNoua.append(obiect)
    
    return listaNoua




    
    