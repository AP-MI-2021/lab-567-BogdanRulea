from Tests.testCrud import testAdaugaObiect,testModificareObiect,testStergereObiect, testGetbyId
from Tests.testDomain import testObiect

def runAllTests():
    testObiect()
    testAdaugaObiect()
    testModificareObiect()
    testStergereObiect()
    testGetbyId()