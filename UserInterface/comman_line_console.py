from Logic.CRUD import AdaugaObiectLista, ModificareObiectLista, StergereObiectLista
from UserInterface.console import  uiShowAll
from Domain.InventarObject import toString

def PrintMenu():
    print("1. Scrie comenzile impreuna cu parametrii corespunzatori(add/delete/showall),functiile si parametrii sunt separati de \';\'")
    print("x. Program incheiat/Schimba meniul")

def OneLineCommand(lista_comenzi,lista : list):
    lista_comenzi = lista_comenzi.split(";")
    i = 0
    try:
        while i < len(lista_comenzi):
            try:
                if lista_comenzi[i] == 'add':
                    lista = AdaugaObiectLista(lista_comenzi[i+1],lista_comenzi[i+2],lista_comenzi[i+3],float(lista_comenzi[i+4]),lista_comenzi[i+5], lista)
                    i+=5
                elif lista_comenzi[i] == 'delete':
                    lista = StergereObiectLista(lista_comenzi[i+1], lista)
                    i+=1
                elif lista_comenzi[i] == 'showall':
                    uiShowAll(lista)
                else:
                    print("Ai scris o comanda invalida")
            except IndexError:
                print("Nu ai adaugat suficienti parametrii.")
            i+=1
    except ValueError as ve:
        print("Error: {}".format(ve))
    return lista

def uiOneLineCommand(lista):
    lista_comenzi = input("Commands format:\nadd;id;nume;descriere;pret achizitie;locatie;\ndelete;id;\nshowall\nScrie comenzile dupa formatul de mai sus, intr-o singura lineie: ")
    return OneLineCommand(lista_comenzi, lista)

def runMenu(lista):
    while True:
        PrintMenu()
        comanda = input("Scrie comanda corespunzatoare din meniu: ")
        if comanda == '1':
            lista = uiOneLineCommand(lista)
        elif comanda == 'x':
            print("Program incheiat!")
            break
        else:
            print("Comanda invalida, incearca din nou!")
