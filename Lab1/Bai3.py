import tkinter as tk 
from tkinter import ttk

win = tk.Tk()

win.title("Vo Dinh Ngoc Binh")

ttk.Label(win, text="A label").grid(column=0, row=0)

win.mainloop()