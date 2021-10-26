from Domain.InventarObject import *

def testObiect():
    obiect = CreazaObiect("1", "televizor", "full hd", 1300, "zzhd")

    assert getId(obiect) == "1"
    assert getNume(obiect) == "televizor"
    assert getDescriere(obiect) == "full hd"
    assert getPretAchizitie(obiect) == 1300.0
    assert getLocatie(obiect) == "zzhd"

