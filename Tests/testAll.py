from Tests.testCrud import testAdaugaObiect,testModificareObiect,testStergereObiect, testGetbyId
from Tests.testDomain import testObiect
from Tests.testFunctionalitati import testMoveAll,testConcatenareDescriere
def runAllTests():
    testObiect()
    testAdaugaObiect()
    testModificareObiect()
    testStergereObiect()
    testGetbyId()
    testMoveAll()
    testConcatenareDescriere()