from os import name, system
def clearTerminal() -> None:
    if name == 'nt':
        system("cls")
    else:
        system("clear")

