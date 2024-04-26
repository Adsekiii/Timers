import time
import clearTerminal

def timer() -> None :
    print("Enter the time you want to finish in [minutes:seconds]: ",end=" ")
    timeToFinish = input()
    minutes = int(timeToFinish[:timeToFinish.find(":")])    #minutes are the value of inputted string up to colon
    seconds = int(timeToFinish[timeToFinish.find(":")+1:])  #seconds are the value of inputted string from colon plus one
    clearTerminal.clearTerminal()
    checkTime(minutes,seconds)  #checking if the entered value is a valid one
    for i in range(minutes*60+seconds): #looping through 
        minutes,seconds = startTimer(minutes,seconds)   #overwriting current minutes and seconds value 
        time.sleep(1)
        
def startTimer(minutes : int, seconds : int) -> int : 
    clearTerminal.clearTerminal()
    print("Time left: ", end="")
    print(minutes , " : " , seconds)
    if minutes != 0:        #if minutes are not equal to 0
        if seconds == 0:    #if seconds equal to 0
            seconds = 60
            minutes -=1
        seconds -= 1    
    else:
        if seconds != 0:    #if there is no minutes left go through seconds that are left 
            seconds -=1
        else:
            clearTerminal.clearTerminal()
            print("Ring! Ring! Ring!")
    return minutes, seconds   

def checkTime(minutes, seconds) -> None :
    errorNum : int = 0
    if type(minutes) != int or minutes < 0:    #if there are any problems with value increase error Number
        print("invalid minuets value")
        errorNum += 1
    if type(seconds) != int or seconds > 59 or seconds < 0:
        print("invalid seconds value")
        errorNum += 1
    if errorNum != 0:   #if error number is not equal to 0 then try again
        print("Please Try again!")
        timer()
    
    