import tkinter as tk     # Python 3.x
from tkinter import ttk

class ComboboxSelectionWindow():
    def __init__(self, master):

        self.dict = {'Choice 1': 1,'Second choice':2, 'Something':3}
        self.master=master
        self.entry_contents=None
        self.labelTop = tk.Label(master,text = "Select one of the following")
        self.labelTop.place(x = 20, y = 10, width=140, height=10)
        self.comboBox_example = ttk.Combobox(master,values=["Choice 1","Second choice","Something","Else"])
        self.comboBox_example.current(0)
        self.comboBox_example.place(x = 20, y = 30, width=140, height=25)

        self.okButton = tk.Button(master, text='OK',command = self.callback)
        self.okButton.place(x = 20, y = 60, width=140, height=25)

    def callback(self):
        """ get the contents of the Entry and exit
        """
        self.comboBox_example_contents=self.comboBox_example.get()
        print(self.dict[self.comboBox_example_contents])
        # self.master.destroy()

def ComboboxSelection():

    app = tk.Tk()
    app.geometry('180x100')
    Selection=ComboboxSelectionWindow(app)
    app.mainloop()

    print("Selected interface: ", Selection.comboBox_example_contents)

    return Selection.comboBox_example_contents

print("Tkinter combobox text selected =", ComboboxSelection())