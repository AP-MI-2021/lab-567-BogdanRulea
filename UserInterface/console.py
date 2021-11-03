from Logic.CRUD import AdaugaObiectLista, ModificareObiectLista, StergereObiectLista
from Domain.InventarObject import toString
from Logic.functionalitati import MoveAll, ConcatenareDescriere
def PrintMenu():
    print("1. Adauga obiect.")
    print("2. Modifica obiect.")
    print("3. Sterge obiect.")
    print("4. Afisare obiecte din inventar.")
    print("5. Muta toate obiectele dintr-o locatie in alta.")
    print("6. Concateneaza descrierile cu un text dat al tuturor obiectelor cu pretul mai mare decat un pret dat.")
    print("x. Program incheiat/Sau schimba meniul.")


def uiAdaugaObiect(lista):
    id = input("Scrie id-ul: ")
    nume = input("Scrie numele obiectului: ")
    descriere = input("Scrie descrierea obiectului: ")
    pret = float(input("Scrie pretul achizitiei obectului: "))
    locatie = input("Scrie locatia obiectului: ")

    return AdaugaObiectLista(id, nume, descriere, pret, locatie, lista)

def uiModificaObiect(lista):
    id = input("Scrie id-ul obiectului de modificat: ")
    nume = input("Scrie noul nume al obiectului: ")
    descriere = input("Scrie noua descriere al obiectului: ")
    pret = float(input("Scrie noul pret al obectului: "))
    locatie = input("Scrie noua locatia a obiectului: ")

    return ModificareObiectLista(id, nume, descriere, pret, locatie, lista)


def uiStergereObiect(lista):
    id = input("Scrie id-ul obiectului de sters: ")

    return StergereObiectLista(id, lista)
def uiMoveAll(lista):
    locatie_init = input("Scrie locatia intiala a obiectului pe care vrei sa il muti: ")
    locatie_nou = input("Scrie noua locatie: ")
    return MoveAll(locatie_init,locatie_nou, lista)

def uiConcatenareDescriere(lista):
    textNou = input("Scrie textul care trebuie adaugat la descriere: ")
    pret = float(input("Scrie pretul: "))
    return ConcatenareDescriere(textNou,pret,lista)

def uiShowAll(lista):
    print("Obiectele din inventar sunt: ")
    for obiect in lista:
        print(toString(obiect))

def runAll(lista):
    running = True
    while running:
        PrintMenu()
        optiune = input("Alege o optiune: ")
        if optiune == '1':
            lista = uiAdaugaObiect(lista)
        elif optiune == '2':
            lista = uiModificaObiect(lista)
        elif optiune == '3':
            lista = uiStergereObiect(lista)
        elif optiune == '4':
            uiShowAll(lista)
        elif optiune == '5':
            lista = uiMoveAll(lista)
        elif optiune == '6':
            lista = uiConcatenareDescriere(lista)
        elif optiune == 'x':
            print("Program incheiat!")
            running = False
        else:
            print("Ai ales o optiune inexistenta, incearca din nou: ")
