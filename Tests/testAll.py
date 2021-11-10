from Tests.testCrud import testAdaugaObiect,testModificareObiect,testStergereObiect, testGetbyId
from Tests.testDomain import testObiect
from Tests.testFunctionalitati import testMoveAll,testConcatenareDescriere, testOrdonareObiecte, testCelMaiMarePretPerLocatie,testSumaPreturilorPerLocatie
from Tests.testUndoRedo import testUndoRedo
def runAllTests():
    testObiect()
    testAdaugaObiect()
    testModificareObiect()
    testStergereObiect()
    testGetbyId()
    testMoveAll()
    testConcatenareDescriere()
    testOrdonareObiecte()
    testCelMaiMarePretPerLocatie()
    testSumaPreturilorPerLocatie()
    testUndoRedo()