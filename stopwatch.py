import time
import clearTerminal
import keyboard

def stopwatch():
    ms = 0
    print("Start by clicking the button (key) <F> ") 
    print("Time by clicking the button (key) <T> ")
    print("Stop by clicking the button (key) <S> ")
    if keyboard.read_key() == "f":
        while True:
            ms = startStopwatch(ms)
            if keyboard.is_pressed("s"):
                break
            else:
                pass
            
        
        
def startStopwatch(ms):
    time.sleep(1/20)
    clearTerminal.clearTerminal()
    ms += 5
    print(int(ms/100), " : ", ms%100)
    return ms
    
        
    
def timeStopwatch():
    pass
