import pandas as pd 
import requests as req 

# class init_file:

#     def __init__(self):

#         config = configparser.ConfigParser()
#         config.read('D:/My_Projects/Python/petrol_fuel_price/config/config.ini')

from tkinter import *

def converter():
    # Create functions for conversion
    def cel_fahr():
        res = int(entry.get()) * 9/5 +32
        print (res)
    def fahr_cel():
        res = (int(entry.get()) - 32) * 5/9
        print (res)

    #Options list for the dropdown
    list_opt = ['Celsius to Fahrenheit', 'Fahrenheit to Celsius']
    # Create the main window 
    root = Tk()
    # Rename the title of the window    
    root.title("Temperature Converter")
    # Set the size of the window
    root.geometry("250x250")
    # Set resizable FALSE
    root.resizable(0,0)
    # Create a variable for the default dropdown option 
    var1 = StringVar()
    # Set the default drop down option 
    var1.set(list_opt[0])
    # Create the dropdown menu 
    dropdown = OptionMenu(root, var1, *list_opt)
    dropdown.configure(state="active")
    # Place the dropdown menu
    dropdown.place(x=45, y=10)

    # Create an entry 
    entry = Entry(root)
    entry.place (x=47, y=60)

    #Create a button 
    button = Button(root, text='Convert', command=cel_fahr)
    button.place(x=85,y=90)

    #I TRIED THIS BUT NO            
    #if var1 == list_opt[0]:
    #button = Button(root, text='Convert', command=cel_fahr)
    #button.place(x=85,y=90)
    #if var1 == list_opt[1]:
    #button = Button(root, text='Convert', command=fahr_cel)
    #button.place(x=85,y=90)


    root.mainloop()



converter()