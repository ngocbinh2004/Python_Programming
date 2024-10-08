import tkinter as tk

# Create instance of tkinter
win = tk.Tk()

# Assign tkinter Variable to strData variable
strData = tk.StringVar()

# Set value of strData variable (use set method of StringVar)
strData.set("Hello StringVar")

# Get value of strData variable (use get method of StringVar)
varData = strData.get()

# Print out current value of strData
print(varData)

#Print out the dafault tkinter variable values
print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())