import tkinter as tk
win = tk.Tk()

def usingGlobal():
    # Try to print the value of GLOBAL_CONST before it's assigned in the local scope
    print(GLOBAL_CONST)  
    GLOBAL_CONST = 777  # Assignment happens after the print statement
    print(GLOBAL_CONST)

usingGlobal()
