import stopwatch
import pomodoro
import timer
import clearTerminal
from tkinter import Tk, ttk, N, S, W, E, StringVar

class window:
    
    def __init__(self, root : Tk) -> None:
        root.title("Timers")
        mainframe = ttk.Frame(root, padding="10 10 20 20")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # ttk.Button(mainframe, text="timer", ).grid(column=1, row=1, sticky=(W))
        # ttk.Button(mainframe, text="stopwatch").grid(column=1, row=2, sticky=(W))
        # ttk.Button(mainframe, text="pomodoro").grid(column=1, row=2, sticky=(W))
        
        # root.title("Timers Menu")
        # mainframe = ttk.Frame(root, padding="5 5 15 15")
        # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)
        
        # self.interfaceInput = StringVar()
        # self.output = StringVar()
        # interfaceInput_entry = ttk.Entry(mainframe, width=7, textvariable=self.interfaceInput)
        # interfaceInput_entry.grid(column=1, row=1, sticky=(W, E))
        
        # ttk.Label(mainframe, textvariable=self.output).grid(column=1, row=2, sticky=(S))
        # ttk.Label(mainframe, text="Input").grid(column=2, row=1, sticky=(W, E))
        # ttk.Button(mainframe, text="change value", command=self.startAction).grid(column=2, row=2, sticky=(S))

        # interfaceInput_entry.focus()
        # root.bind("<Return>", self.startAction)

    def startAction(self, *args):
        try:
            value = str(self.interfaceInput.get())
            self.output.set(value)
        except ValueError:
            pass
        
class interface:
    def __init__(self, root):
        root.title("Timers")
        mainframe = ttk.Frame(root, padding="10 10 20 20")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        ttk.Button(mainframe, text="timer", ).grid(column=1, row=1, sticky=(W))
        ttk.Button(mainframe, text="stopwatch").grid(column=1, row=2, sticky=(W))
        ttk.Button(mainframe, text="pomodoro").grid(column=1, row=3, sticky=(W))
        
root = Tk()
interface(root)
window(root)
root.mainloop()