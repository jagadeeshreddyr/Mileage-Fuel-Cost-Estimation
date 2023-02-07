import tkinter  as tk
from tkinter import ttk
import pandas as pd 
import requests
'''
# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame, tk):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        tk.__init__(self, master) 

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Fuel Check")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        Label(self.master, text='Choose City', bd=6).grid(row=0, column=0,pady=(5,5))

        # creating a button instance
        # quitButton = Button(self, text="Exit",command=self.client_exit)

        # placing the button on my window
        # quitButton.place(x=0, y=0)



    def client_exit(self):
        exit()
'''
class label():

    def __init__(self, master=None):

        self.master = master
        # Label.__init__(self, self.master)   
        # ttk.Combobox.__init__(self, self.master) 

        
        url = 'https://economictimes.indiatimes.com/wealth/fuel-price/petrol'
        html = requests.get(url).content 
        self.data = pd.read_html(html)[0]

    
        self.fuel_data

        self.tk = tk.Label(self.master, text='Choose City', bd=6).grid(row=0, column=0,pady=(5,5))
        self.variable = tk.StringVar(self.master)
        self.variable.set("Not Selected")
        self.combox = ttk.Combobox(self.master,  values=list(self.fuel_data.keys()), justify="center", textvariable = self.variable,width=20)
        self.combox.bind('<<ComboboxSelected>>', self.callback())
        self.okButton = tk.Button(self.master, text='OK',command = self.callback)
        # self.okButton.place(x = 20, y = 60, width=140, height=25)

        #  self.data.city.values.tolist()

    def callback(self):
        """ get the contents of the Entry and exit
        """
        self.comboBox_example_contents=self.comboBox_example.get()
        print(self.fuel[self.comboBox_example_contents])


    @property
    def fuel_data(self):
        self.fuel = {row['city'] : row['Petrol Price'] for count, row in self.data.iterrows() }
        return self.fuel






    # def row1(self):
    #     Label(self.master, text='Choose City', bd=6).grid(row=0, column=0,pady=(5,5))
    #     variable = StringVar(self.master)
    #     variable.set("Not Selected")
    #     w = ttk.Combobox(self.master,  values=list(self.fuel_data.keys()), justify="center", textvariable = variable,width=20)
    #     w.bind('<<ComboboxSelected>>', self.callback(w))
    #     w.grid(row=0, column = 2)


if __name__ == "__main__":

    # root window created. Here, that would be the only window, but
    # you can later have windows within windows.
    root = tk.Tk()

    root.geometry("600x400")

    #creation of an instance
    app = label(root)

    #mainloop 
    root.mainloop()