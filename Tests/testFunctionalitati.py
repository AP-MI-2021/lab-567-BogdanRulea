from Logic.CRUD import AdaugaObiectLista, ModificareObiectLista
from Logic.functionalitati import MoveAll, ConcatenareDescriere, CelMaiMarePretPerLocatie, OrdonareObiecte, SumaPreturilorPerLocatie

def testMoveAll():
    lista = []
    lista = AdaugaObiectLista("1", "televizor", "full hd", 1300, "zzhd", lista)
    lista = AdaugaObiectLista("2", "frigider", "A+++", 600, "zjjd", lista)
    lista = AdaugaObiectLista("3", "aragaza", "4 ochiuri", 750, "zzhd", lista)

    assert MoveAll("zzhd", "zzzz", lista) == [[('id', '1'), ('nume', 'televizor'), ('descriere', 'full hd'), ('PretAchizitie', 1300.0), ('locatie', 'zzzz')], [('id', '2'), ('nume', 'frigider'), ('descriere', 'A+++'), ('PretAchizitie', 600.0), ('locatie', 'zjjd')], [('id', '3'), ('nume', 'aragaza'), ('descriere', '4 ochiuri'), ('PretAchizitie', 750.0), ('locatie', 'zzzz')]]
    assert MoveAll("aaaa", "asdd", lista) == lista

def testConcatenareDescriere():
    lista = []
    lista = AdaugaObiectLista("1", "televizor", "full hd", 1300, "zzhd", lista)
    lista = AdaugaObiectLista("2", "frigider", "A+++", 600, "zjjd", lista)
    lista = AdaugaObiectLista("3", "aragaza", "4 ochiuri", 750, "zzhd", lista)

    assert ConcatenareDescriere(" Nou", 500, lista) == [[('id', '1'), ('nume', 'televizor'), ('descriere', 'full hd Nou'), ('PretAchizitie', 1300.0), ('locatie', 'zzhd')], [('id', '2'), ('nume', 'frigider'), ('descriere', 'A+++ Nou'), ('PretAchizitie', 600.0), ('locatie', 'zjjd')], [('id', '3'), ('nume', 'aragaza'), ('descriere', '4 ochiuri Nou'), ('PretAchizitie', 750.0), ('locatie', 'zzhd')]]
    assert ConcatenareDescriere(" Nou", 1500, lista) == lista


def testCelMaiMarePretPerLocatie():
    lista = []
    lista = AdaugaObiectLista("1", "televizor", "full hd", 1300, "zzhd", lista)
    lista = AdaugaObiectLista("2", "frigider", "A+++", 600, "zjjd", lista)
    lista = AdaugaObiectLista("3", "aragaza", "4 ochiuri", 750, "zzhd", lista)

    assert CelMaiMarePretPerLocatie(lista) == {"zjjd":600, "zzhd" : 1300}
    lista = ModificareObiectLista("3","aragaz", "electric", 750, "aaaa", lista)

    assert CelMaiMarePretPerLocatie(lista) == {"aaaa" : 750, "zjjd" : 600, "zzhd" : 1300}

def testOrdonareObiecte():
    lista = []
    lista = AdaugaObiectLista("1", "televizor", "full hd", 1300, "zzhd", lista)
    lista = AdaugaObiectLista("2", "frigider", "A+++", 600, "zjjd", lista)
    lista = AdaugaObiectLista("3", "aragaza", "4 ochiuri", 750, "zzhd", lista)

    assert OrdonareObiecte(lista) == [[('id', '2'), ('nume', 'frigider'), ('descriere', 'A+++'), ('PretAchizitie', 600.0), ('locatie', 'zjjd')],
                                      [('id', '3'), ('nume', 'aragaza'), ('descriere', '4 ochiuri'), ('PretAchizitie', 750.0), ('locatie', 'zzhd')],
                                      [('id', '1'), ('nume', 'televizor'), ('descriere', 'full hd'), ('PretAchizitie', 1300.0), ('locatie', 'zzhd')]]


def testSumaPreturilorPerLocatie():
    lista = []
    lista = AdaugaObiectLista("1", "televizor", "full hd", 1300, "zzhd", lista)
    lista = AdaugaObiectLista("2", "frigider", "A+++", 600, "zjjd", lista)
    lista = AdaugaObiectLista("3", "aragaza", "4 ochiuri", 750, "zzhd", lista)

    assert SumaPreturilorPerLocatie(lista) == {"zjjd" : 600, "zzhd" : 2050}

    lista = ModificareObiectLista("2", "frigider", "A+++", 600, "zzhd", lista)

    assert SumaPreturilorPerLocatie(lista) == {"zzhd" : 2650}


