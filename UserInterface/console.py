from Logic.CRUD import AdaugaObiectLista, ModificareObiectLista, StergereObiectLista
from Domain.InventarObject import toString
from Logic.functionalitati import MoveAll, ConcatenareDescriere, OrdonareObiecte, SumaPreturilorPerLocatie, CelMaiMarePretPerLocatie
def PrintMenu():
    print("1. Adauga obiect.")
    print("2. Modifica obiect.")
    print("3. Sterge obiect.")
    print("4. Muta toate obiectele dintr-o locatie in alta.")
    print("5. Concateneaza descrierile cu un text dat al tuturor obiectelor cu pretul mai mare decat un pret dat.")
    print("6. Cel mai mare pret pentru fiecare locatie.")
    print("7. Ordonarea obiectelor crescator dupa pret.")
    print("8. Afisarea sumelor preturilor pentru fiecare locatie.")
    print("a. Afisare obiecte din inventar.")
    print("u. Undo.")
    print("r. Redo.")
    print("x. Program incheiat/Sau schimba meniul.")


def uiAdaugaObiect(lista):
    try:
        id = input("Scrie id-ul: ")
        nume = input("Scrie numele obiectului: ")
        descriere = input("Scrie descrierea obiectului: ")
        pret = float(input("Scrie pretul achizitiei obectului: "))
        locatie = input("Scrie locatia obiectului: ")
        
        return AdaugaObiectLista(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista

def uiModificaObiect(lista):
    try:
        id = input("Scrie id-ul obiectului de modificat: ")
        nume = input("Scrie noul nume al obiectului: ")
        descriere = input("Scrie noua descriere al obiectului: ")
        pret = float(input("Scrie noul pret al obectului: "))
        locatie = input("Scrie noua locatia a obiectului: ")
        rezultat = ModificareObiectLista(id, nume, descriere, pret, locatie, lista)
        return rezultat
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista



def uiStergereObiect(lista):
    try:
        id = input("Scrie id-ul obiectului de sters: ")
        return StergereObiectLista(id, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def uiMoveAll(lista):
    try:
        locatie_init = input("Scrie locatia intiala a obiectului pe care vrei sa il muti: ")
        locatie_nou = input("Scrie noua locatie: ")
       
        return MoveAll(locatie_init,locatie_nou, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def uiConcatenareDescriere(lista):
    try:
        textNou = input("Scrie textul care trebuie adaugat la descriere: ")
        pret = float(input("Scrie pretul: "))
       
        return ConcatenareDescriere(textNou,pret,lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def uiShowAll(lista):
    try:
        for obiect in lista:
            print(toString(obiect))
    except ValueError as ve:
        print("Eroare {}".format(ve))



def uiCelMaiMarePretPerLocatie(lista):
    print("Lista preturilor pentru fiecare locatie este: ")
    rez = CelMaiMarePretPerLocatie(lista)
    for locatie in rez.keys():
        print(f"{locatie} - {rez[locatie]}")

def uiOrdonareObiecte(lista):
    return OrdonareObiecte(lista)

def uiSumaPreturilorPerLocatie(lista):
    print("Suma preturilor pentru fiecare locatie este: ")
    rez = SumaPreturilorPerLocatie(lista)
    for locatie in rez.keys():
        print(f"{locatie}  - {rez[locatie]}")

def runAll(lista):
    running = True
    undolst = []
    redolst = []
    while running:
        PrintMenu()
        optiune = input("Alege o optiune: ")
        if optiune == '1':
            undolst.append(lista)
            redolst.clear()
            lista = uiAdaugaObiect(lista)
        elif optiune == '2':
            undolst.append(lista)
            redolst.clear()
            lista = uiModificaObiect(lista)
        elif optiune == '3':
            undolst.append(lista)
            redolst.clear()
            lista = uiStergereObiect(lista)
        elif optiune == 'a':
            uiShowAll(lista)
        elif optiune == '4':
            undolst.append(lista)
            redolst.clear()
            lista = uiMoveAll(lista)
        elif optiune == '5':
            undolst.append(lista)
            redolst.clear()
            lista = uiConcatenareDescriere(lista)
        elif optiune == '6':
            uiCelMaiMarePretPerLocatie(lista)
        elif optiune == '7':
            lista = uiOrdonareObiecte(lista)
        elif optiune == '8':
            uiSumaPreturilorPerLocatie(lista)
        elif optiune == 'u':
            if len(undolst) > 0:
                redolst.append(lista)
                lista = undolst.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redolst) > 0:
                undolst.append(lista)
                lista = redolst.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == 'x':
            print("Program incheiat!")
            running = False
        else:
            print("Ai ales o optiune inexistenta, incearca din nou: ")
