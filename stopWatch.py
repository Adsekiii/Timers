import time
import clearTerminal
import keyboard

def stopwatch():
    ms = 0
    timedTime : list = []
    print("Start by clicking the button (key) <F> ") 
    print("Time by clicking the button (key) <T> ")
    print("Stop by clicking the button (key) <S> ")
    if keyboard.read_key() == "f":
        while True:
            ms = startStopwatch(ms)
            showTimed(ms, timedTime)
            if keyboard.is_pressed("s"):
                break
            elif keyboard.is_pressed("t"):
                timeStopwatch(timedTime,ms)
            else:
                pass
            
        
        
def startStopwatch(ms):
    time.sleep(1/20)
    clearTerminal.clearTerminal()
    ms += 5
    return ms
    
def timeStopwatch(timedTime, currTime) -> list:
    timedTime.append(str(int(currTime/100)) + " : " + str(currTime%100))
    return timedTime

def showTimed(currTime, timedTime):
    print(int(currTime/100), " : ", currTime%100)
    i = 1
    for x in timedTime:
        print(i, "| ",x)
        i+=1
        
