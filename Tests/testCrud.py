from Logic.CRUD import AdaugaObiectLista, StergereObiectLista, ModificareObiectLista, GetById
from Domain.InventarObject import getId, getNume, getLocatie, getPretAchizitie, getDescriere

def testAdaugaObiect():
    lista = []

    lista = AdaugaObiectLista("1", "televizor", "full hd", 1300, "zzhd", lista)

    assert len(lista) == 1
    assert getId(GetById("1",lista)) == "1"
    assert  getNume(GetById("1",lista)) == "televizor"
    assert  getDescriere(GetById("1",lista)) == "full hd"
    assert getPretAchizitie(GetById("1", lista)) == 1300.0
    assert  getLocatie(GetById("1",lista)) == "zzhd"

def testModificareObiect():
    lista = []
    lista = AdaugaObiectLista("1", "televizor", "full hd", 1300, "zzhd", lista)
    lista = AdaugaObiectLista("2", "frigider", "A+++", 600, "zjjd", lista)

    lista = ModificareObiectLista("2", "aragaz", "4 ochiuri, electric", 550, "zzhz", lista)


    obiect = GetById("1", lista)

    assert getId(obiect) == "1"
    assert getNume(obiect) == "televizor"
    assert getDescriere(obiect) == "full hd"
    assert getPretAchizitie(obiect) == 1300.0
    assert getLocatie(obiect) == "zzhd"

    obiect = GetById("2", lista)

    assert getId(obiect) == "2"
    assert getNume(obiect) == "aragaz"
    assert getDescriere(obiect) == "4 ochiuri, electric"
    assert getPretAchizitie(obiect) == 550.0
    assert getLocatie(obiect) == "zzhz"

def testStergereObiect():
    lista = []
    lista = AdaugaObiectLista("1", "televizor", "full hd", 1300, "zzhd", lista)
    lista = AdaugaObiectLista("2", "frigider", "A+++", 600, "zjjd", lista)

    lista = StergereObiectLista("1", lista)
    assert len(lista) == 1

    assert GetById("1", lista) is None
    assert GetById("2", lista) is not None

    lista = StergereObiectLista("3", lista)

    assert  len(lista) == 1
    assert GetById("1", lista) is None
    assert GetById("2", lista) is not None

