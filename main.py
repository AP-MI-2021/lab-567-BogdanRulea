from UserInterface.console import runAll
from Tests.testAll import runAllTests
from UserInterface.comman_line_console import runMenu

def mainMenu():
    print("1. Consola normala.")
    print("2. Consola command-line-meniu.")

def main():
    runAllTests()
    lista = []
    mainMenu()

    meniu = input("Alege meniul: ")
    while True:
        if meniu == '1':
            runAll(lista)
        elif meniu == '2':
            runMenu(lista)
        else:
            print("Meniu neselectat.")
        meniu_nou = input("Vrei sa schimbi meniul? (da/nu): ")
        if meniu_nou.lower() == 'da':
            mainMenu()
            meniu = input("Alege meniul: ")
        elif meniu_nou.lower() == 'nu':
            break
        else:
            print("Ai ales o optiune invalida, incearca din nou: ")
            meniu = 0

main()

