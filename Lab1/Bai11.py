from tkinter import ttk
import tkinter as tk 
from tkinter import scrolledtext

win = tk.Tk()

win.title("Vo Dinh Ngoc Binh")

ttk.Label(win, text="A label").grid(column=0, row=0)

def click_me():
   
    action.configure(text='Hello ' + name.get())

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)    

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)
name_entered.focus()

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def radCall():
    radSel=radVar.get()
    if radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure (background=COLOR2)
    elif radSel == 3: win.configure (background=COLOR3)


radVar = tk.IntVar()

rad1 = tk.Radiobutton (win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk. Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk. Radiobutton (win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

colors = ["Blue", "Gold", "Red"]

def radCall():
  radSel = radVar.get()
  if radSel == 0: win.configure(background=colors[0]) # now zero-based
  elif radSel == 1: win.configure(background=colors[1]) # and using list
  elif radSel == 2: win.configure(background=colors[2])
radVar = tk.IntVar()

radVar.set(99)
for col in range(3):
  curRad = tk.Radiobutton(win, text=colors[col], variable=radVar,
  value=col, command=radCall)
  curRad.grid(column=col, row=5, sticky=tk.W)

name_entered.focus()

win.mainloop()