from Domain.InventarObject import getLocatie, getPretAchizitie, toString, getId, getNume, getDescriere
from Logic.CRUD import AdaugaObiectLista, ModificareObiectLista


def MoveAll(locatie, locatie_noua, lista):
    """Muta toate obiectele dintr-o locatie in alta

    Args:
        locatie (4 chars): locatie initiala
        locatie_noua (4 chars): locatie finala
        lista (list[int]): lista data
    """

    lista_noua = lista
    for obiect in lista:
        if getLocatie(obiect) == locatie:
            lista_noua = ModificareObiectLista(getId(obiect), getNume(obiect), getDescriere(obiect), getPretAchizitie(obiect), locatie_noua, lista_noua)

    return lista_noua

def ConcatenareDescriere(textNou, pret, lista):
    """Concatenarea unui string citit descrierii obiectelor cu un pret mai mare decat cel dat

    Args:
        textNou (string): text de concatenat
        pret (float): pret dat
        lista (list[int]): lista data
    """
    listaNoua = lista
    for obiect in lista:
        if getPretAchizitie(obiect) > float(pret):
            listaNoua = ModificareObiectLista(getId(obiect), getNume(obiect), (getDescriere(obiect) + textNou), getPretAchizitie(obiect),getLocatie(obiect), listaNoua)
    return listaNoua

def CelMaiMarePretPerLocatie(lista):
    """
    Functia calculeaza cele mai mari preturi pentru fiecare locatie

    Args:
        lista: lista cu obiecte din inventar

    Returns: lista celor mai mari preturi din fiecare locatie

    """
    listaPreturi = {}
    for obiect in lista:
        if getLocatie(obiect) not in listaPreturi.keys():
            listaPreturi[getLocatie(obiect)] = getPretAchizitie(obiect)
        elif listaPreturi[getLocatie(obiect)] < getPretAchizitie(obiect):
            listaPreturi[getLocatie(obiect)] = getPretAchizitie(obiect)

    return listaPreturi

def OrdonareObiecte(lista : list):
    """
    Functia ordoneaza crescator obiectele dupa pret
    Args:
        lista: lista cu obiectele din inventar

    Returns: lista ordonata crescator

    """
    listaFinala = lista
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if getPretAchizitie(listaFinala[i]) > getPretAchizitie(listaFinala[j]):
                aux = listaFinala[i]
                listaFinala[i] = listaFinala[j]
                listaFinala[j] = aux

    return listaFinala

def SumaPreturilorPerLocatie(lista):
    '''
    Functia calculeaza suma preturilor obiectelor din fiecare locatie
    Args:
        lista: lista cu obiecte din inventar

    Returns: lista cu suma corespunzatoare locatiilor

    '''
    listaPreturi = {}
    for obiect in lista:
        if getLocatie(obiect) not in listaPreturi.keys():
            listaPreturi[getLocatie(obiect)] = getPretAchizitie(obiect)
        else:
            listaPreturi[getLocatie(obiect)]+=getPretAchizitie(obiect)

    return listaPreturi

