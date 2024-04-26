import time
import clearTerminal
import keyboard

# TODO global variables are not good in python, code need a rewrite to account for that

workPhase : int = 30
shortBreak : int = 5
longBreak : int = 15
workPhaseNumber : int = 0
isItWorkingTime = True

def pomodoro() -> None :
    global workPhaseNumber
    clearTerminal.clearTerminal()
    print("---POMODORO TIMER---")
    print("Start Working phase! -> <F>")
    print("Access options! -> <O>")
    match keyboard.read_key():     #after pressing F start pomodoro
        case 'f':
            # TODO this pice of code need a desperate rewrite with less if statements
            sec : int = workPhase * 60
            while True:
                if isItWorkingTime == True:
                    if sec == 0:
                        sec = workPhase * 60
                    else:
                        sec = startPomodoro(sec)
                else:
                    if sec == 0:
                        workPhaseNumber += 1
                        if workPhaseNumber % 3==0:
                            sec = longBreak * 60
                        else:
                            sec = shortBreak * 60
                    elif workPhaseNumber % 3==0:
                        sec = startLongBreak(sec)
                    else:
                        sec = startShortBreak(sec)
        case "o":
            options()
        case _:
            print("INVALID VALUE! Try again!")
            time.sleep(1)
            pomodoro()

def startPomodoro(sec) -> int : #print current time, check if seconds are equal to 0 then choose which break to start
    global isItWorkingTime
    clearTerminal.clearTerminal()
    print(int(sec/60), ":", sec%60)
    sec -= 1
    time.sleep(1)
    if sec == 0:
        clearTerminal.clearTerminal()
        print(int(sec/60), ":", sec%60)
        print("Work time is over click any key to proceed to break!")
        isItWorkingTime = False
        keyboard.read_key()
    return sec

# TODO short and long break are identical so they should be refactored into singular function eventually
def startShortBreak(sec) -> int :
    global isItWorkingTime
    clearTerminal.clearTerminal()
    print(int(sec/60), ":", sec%60)
    sec -= 1
    time.sleep(1)
    if sec == 0:
        clearTerminal.clearTerminal()
        print(int(sec/60), ":", sec%60)
        print("Short break time is over click any key to proceed to work!")
        isItWorkingTime = True
        keyboard.read_key()
    return sec

def startLongBreak(sec) -> int :
    global isItWorkingTime
    clearTerminal.clearTerminal()
    print(int(sec/60), ":", sec%60)
    sec -= 1
    time.sleep(1)
    if sec == 0:
        clearTerminal.clearTerminal()
        print(int(sec/60), ":", sec%60)
        print("Long break time is over click any key to proceed to work!")
        isItWorkingTime = True
        keyboard.read_key()
    return sec
# TODO cases are similar so maybe add a separate function for it?
def options() -> None :
    global workPhase
    global longBreak
    global shortBreak
    clearTerminal.clearTerminal()
    print("Exit -> <X>")
    print("Customize working time -> <Q>")
    print("Customize long break time -> <W>")
    print("Customize short break time -> <E>")
    match keyboard.read_key():
        case "x":
            clearTerminal.clearTerminal()
            pomodoro()
        case "q":
            workPhase = changeTime()
            clearTerminal.clearTerminal()
            print("successfully changed working time to ", workPhase, " minutes")
            time.sleep(1)
            pomodoro()
        case "w":
            longBreak = changeTime()
            clearTerminal.clearTerminal()
            print("successfully changed long break time to ", longBreak, " minutes")
            time.sleep(1)
            pomodoro()
        case "e":
            
            shortBreak = changeTime()
            clearTerminal.clearTerminal()
            print("successfully changed short break time to ", shortBreak, " minutes")
            time.sleep(1)
            pomodoro()
        case _:
            print("INVALID VALUE! Try again!")
            time.sleep(1)
            options()
             
def changeTime() -> int :
    print("Please enter how long should it lasts in minutes: ",end="")
    type = input()
    type = int(type)
    return type