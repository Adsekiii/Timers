from os import name, system
def clearTerminal() -> None :
    if name == 'nt':    #if os is Windows
        system("cls")
    else:               #else if its either Mac or Linux
        system("clear")

