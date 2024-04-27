import time
import clearTerminal

# TODO Add gui and sound effects 
# TODO Add invalid time input handling
# TODO Add 'stop' button so that you can stop anytime
# TODO after stop add display amount of cycles that user lasted as well as overall time worked and rested

def pomodoroSetup() -> None :
    workingTime : str = "10:10"
    shortBreakTime : str = "0:02"
    longBreakTime : str = "0:10"
    working : bool = True
    cycles : int = 0
    
    while True:
        print("####POMODORO####")
        print("1. Start Pomodoro")
        print("2. Change Time")
        print("3. Back")
        choice : str = input()
    
        match choice:
            case '1':
                clearTerminal.clearTerminal()
                pomodoro(workingTime, shortBreakTime, longBreakTime, working, cycles)
                clearTerminal.clearTerminal()
            case '2':
                clearTerminal.clearTerminal()
                workingTime, shortBreakTime, longBreakTime = timeSettings(workingTime, shortBreakTime, longBreakTime)
                clearTerminal.clearTerminal()
            case '3':
                break
            case _:
                clearTerminal.clearTerminal()
                print("invalid option try again!")
        
def timeSettings(workingTime,shortBreakTime,longBreakTime) -> tuple[str,str,str] :
    print("Which time do you want to change?")
    print("1. Work time")
    print("2. Short break")
    print("3. Long break")
    choice : str = input()
    match choice:
        case '1':
            clearTerminal.clearTerminal()
            workingTime = timeChange(workingTime)
        case '2':
            clearTerminal.clearTerminal()
            shortBreakTime = timeChange(shortBreakTime)
        case '3':
            clearTerminal.clearTerminal()
            longBreakTime = timeChange(longBreakTime)
        case _:
            print("invalid option try again!")
            timeSettings()
    return workingTime, shortBreakTime, longBreakTime

def pomodoro(workingTime : str, shortBreakTime : str, longBreakTime : str, working : bool , cycles : int) -> None:
    while True:
        # TODO write a function for time assignment for 'seconds' variable
        if cycles % 3 is 0 and working is False:
            seconds : int = int(longBreakTime[:longBreakTime.find(":")])*60 + int(longBreakTime[longBreakTime.find(":")+1:])
            print("Long break time!")
            time.sleep(2)
            countdown(seconds) 
            working = not working 
        elif cycles % 3 is not 0 and working is False:
            seconds : int  = int(shortBreakTime[:shortBreakTime.find(":")])*60 + int(shortBreakTime[shortBreakTime.find(":")+1:])
            print("Short break time!")
            time.sleep(2)
            countdown(seconds) 
            working = not working 
        else:
            seconds : int  = int(workingTime[:workingTime.find(":")])*60 + int(workingTime[workingTime.find(":")+1:])
            print("Working time!")
            time.sleep(2)
            countdown(seconds)
            cycles += 1
            working = not working 

def timeChange(timeToChange : str) -> str :
    print("Specify how long should it last in mm:ss format: ",end="")
    ################ TODO add error handling ################
    timeToChange : str = input()
    return timeToChange

def countdown(seconds) -> None:
    for i in range(seconds+1):
        clearTerminal.clearTerminal()
        print(f"{"0" if int(seconds/60) < 10 else ""}{int(seconds/60)} : {"0" if seconds%60 < 10 else ""}{int(seconds%60)}")
        seconds -= 1
        time.sleep(1) 
 