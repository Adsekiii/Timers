import time
import clearTerminal

def timer():
    print("Enter the time you want to finish in [minutes:seconds]: ",end=" ")
    timeToFinish = input()
    minutes = int(timeToFinish[:timeToFinish.find(":")])
    seconds = int(timeToFinish[timeToFinish.find(":")+1:])
    clearTerminal.clearTerminal()
    checkTime(minutes,seconds)
    for i in range(minutes*60+seconds):
        minutes,seconds = startTimer(minutes,seconds)
        time.sleep(1)
        
    
def startTimer(minutes : int, seconds : int):
    clearTerminal.clearTerminal()
    print("Time left: ", end="")
    print(minutes , " : " , seconds)
    if minutes != 0:
        if seconds == 0:
            seconds = 60
            minutes -=1
        seconds -= 1
    else:
        if seconds != 0:
            seconds -=1
        else:
            stopTimer()
    return minutes, seconds
            
        
    
def stopTimer():
    clearTerminal.clearTerminal()
    print("Ring! Ring! Ring!")

def checkTime(minutes, seconds):
    errorNum : int = 0
    if type(minutes) != int:
        print("invalid minuets value")
        errorNum += 1
    if type(seconds) != int or seconds > 59 or seconds < 0:
        print("invalid seconds value")
        errorNum += 1
    if errorNum != 0:
        print("Please Try again!")
        timer()
    
    