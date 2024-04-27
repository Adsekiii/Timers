import stopwatch
import pomodoro
import timer
import clearTerminal

def menu() -> None :
    
    print("TIMER")
    print("1.Stop watch")
    print("2.timer")
    print("3.Pomodoro")
    choice = input()            #get input from user
    chceckIfValid(choice)       #check if input is recognized
    
def chceckIfValid(choice) -> None :
    match choice:
        case '1':
            stopwatch.stopwatch()   #user chosen stopwatch
        case '2':
            timer.timer()           #user chosen timer
        case '3':
            pomodoro.pomodoroSetup()     #user chosen pomodoro
        case _:
            clearTerminal.clearTerminal()
            print("There is no such value") #user chosen option other than expected
            menu()
    menu()
    
    
        