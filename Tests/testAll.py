from Tests.testCrud import testAdaugaObiect,testModificareObiect,testStergereObiect
from Tests.testDomain import testObiect

def runAllTests():
    testObiect()
    testAdaugaObiect()
    testModificareObiect()
    testStergereObiect()