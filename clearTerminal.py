from os import name, system
def clearTerminal() -> None:
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

