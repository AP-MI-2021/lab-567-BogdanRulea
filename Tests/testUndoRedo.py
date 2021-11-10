from Logic.CRUD import AdaugaObiectLista, ModificareObiectLista, StergereObiectLista


def testUndoRedo():
    undolst = []
    redolst = []
    lista = []
    undolst.append(lista)
    redolst.clear()
    lista = AdaugaObiectLista("1", "televizor", "full hd", 1300, "zzhd", lista)
    #undo
    redolst.append(lista)
    lista = undolst.pop()
    assert lista == []
    #redo
    undolst.append(lista)
    lista = redolst.pop()
    assert lista == [[("id", "1"),("nume","televizor"),("descriere", "full hd"),("PretAchizitie",1300.0),("locatie","zzhd")]]
    
    undolst.append(lista)
    redolst.clear()
    lista = AdaugaObiectLista("2", "frigider", "A+++", 600, "zjjd", lista)
    #undo
    redolst.append(lista)
    lista = undolst.pop()
    assert lista == [[("id", "1"),("nume","televizor"),("descriere", "full hd"),("PretAchizitie",1300.0),("locatie","zzhd")]]

    #redo
    undolst.append(lista)
    lista = redolst.pop()

    assert lista == [[("id", "1"),("nume","televizor"),("descriere", "full hd"),("PretAchizitie",1300.0),("locatie","zzhd")],
                     [("id", "2"),("nume","frigider"),("descriere", "A+++"),("PretAchizitie",600),("locatie","zjjd")]]

    undolst.append(lista)
    redolst.clear()

    lista = ModificareObiectLista("1","televizor","ultra hd", 1350, "zzhd", lista)

    #undo
    redolst.append(lista)
    lista = undolst.pop()
    assert lista ==  [[("id", "1"),("nume","televizor"),("descriere", "full hd"),("PretAchizitie",1300.0),("locatie","zzhd")],
                     [("id", "2"),("nume","frigider"),("descriere", "A+++"),("PretAchizitie",600),("locatie","zjjd")]]
    
    #redo
    undolst.append(lista)
    lista = redolst.pop()
    

    undolst.append(lista)
    redolst.clear()

    lista = StergereObiectLista('2',lista)

    assert lista == [[("id", "1"),("nume","televizor"),("descriere", "ultra hd"),("PretAchizitie",1350.0),("locatie","zzhd")]]
    
    #undo
    redolst.append(lista)
    lista = undolst.pop()

    assert lista ==  [[("id", "1"),("nume","televizor"),("descriere", "ultra hd"),("PretAchizitie",1350.0),("locatie","zzhd")],
                     [("id", "2"),("nume","frigider"),("descriere", "A+++"),("PretAchizitie",600),("locatie","zjjd")]]
    
    #redo
    undolst.append(lista)
    lista = redolst.pop()
    assert lista == [[("id", "1"),("nume","televizor"),("descriere", "ultra hd"),("PretAchizitie",1350.0),("locatie","zzhd")]]

    
