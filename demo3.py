import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected = combo_box.get()
    label.config(text="You selected: " + selected)

root = tk.Tk()

options = ["Option 1", "Option 2", "Option 3"]
combo_box = ttk.Combobox(root, values=options)
combo_box.bind("<<ComboboxSelected>>", on_select)
combo_box.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()