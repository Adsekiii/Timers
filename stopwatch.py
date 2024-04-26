import time
import clearTerminal
import keyboard

def stopwatch() -> None :
    ms : int = 0
    timedTime : list = []           #list of timed values
    print("Start by clicking the button (key) <F> ") 
    print("Time by clicking the button (key) <T> ")
    print("Stop by clicking the button (key) <S> ")
    if keyboard.read_key() == "f":
        while True:
            ms = startStopwatch(ms)             #overwriting value of ms which is milliseconds 
            showTimed(ms, timedTime)            #showing timed values of stopwatch
            if keyboard.is_pressed("s"):        #stopping program 
                break
            elif keyboard.is_pressed("t"):      #time current value of stopwatch
                timeStopwatch(timedTime,ms)
            else:
                pass
             
def startStopwatch(ms) -> int : #sleeping for 1/20 of a second then adding 5ms to current time 
    time.sleep(1/20)
    clearTerminal.clearTerminal()
    ms += 5
    return ms
    
def timeStopwatch(timedTime, currTime) -> list : #adding current time value as string to timed Values list
    timedTime.append(str(int(currTime/100)) + " : " + str(currTime%100))
    return timedTime

def showTimed(currTime, timedTime) -> None : #showing saved time values
    print(int(currTime/100), " : ", currTime%100)
    i = 1
    for x in timedTime:
        print(i, "| ",x)
        i+=1
        
