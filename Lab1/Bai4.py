from tkinter import ttk
import tkinter as tk 

win = tk.Tk()

win.title("Vo Dinh Ngoc Binh")

a_label =ttk.Label(win, text="A label")
a_label.grid(column = 0, row = 0)

def click_me():
    action.configure(text="** I have been Clicked! **")  
    a_label.configure (foreground='red')  
    a_label.configure(text='A Red Label')

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=0)

win.mainloop()