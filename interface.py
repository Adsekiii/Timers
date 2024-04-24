import stopwatch
import pomodoro
import timer
import clearTerminal

def menu():
    
    print("TIMER")
    print("1.Stop watch")
    print("2.timer")
    print("3.Pomodoro")
    choice = input()
    chceckIfValid(choice)
    
def chceckIfValid(choice) -> None:
    try:
        match choice:
            case '1':
                stopwatch.stopwatch()
            case '2':
                timer.timer()
            case '3':
                pomodoro.pomodoro()
            case _:
                print("There is no such value")
    except ValueError:
        clearTerminal.clearTerminal()
        print("There is no such option!\nPlease try again!\n")
        menu()
    
        