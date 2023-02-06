from turtle import width
import requests
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os 

url = 'https://economictimes.indiatimes.com/wealth/fuel-price/petrol'
html = requests.get(url).content 

data = pd.read_html(html)[0]




dicts={}
for count,row in data.iterrows():
    dicts[row['city']]=row['Petrol Price']


# def calculate(mileage, fuel):
#     rate = fuel 

# print(dicts)
def callback(selection):
    print(data.loc[data['city']==selection.widget.get(),'Petrol Price'].values[0].split('₹')[0])


def on_change():
    try:
        print(float(name.widget.get()))
        print(float(name2.widget.get()))
        print(name1.wi)
    except:
        messagebox.showwarning("showwarning", "Please Enter number")

def on_change2(e2):
    try:
        print(float(e2.widget.get()))

    except:
        messagebox.showwarning("showwarning", "Please Enter number")


# def event(ss):
#     print(on_change)


def main():


    root = tk.Tk()
    root.geometry('500x300')
    root.title("Fuel Price Across India")
    # root.configure(bg='grey')
    root.config(bg='#597678')

    tk.Label(root, text='Choose City', bd=6).grid(row=0, column=0,pady=(5,5))
    #tk.grid(row=1, column=1, padx=10, pady=10)


    var_material = tk.StringVar()

    combo_material = ttk.Combobox(root, values=list(dicts.keys()), justify="center", textvariable=var_material,width=20)
    combo_material.bind('<<ComboboxSelected>>', lambda event: label_selected.config(text=dicts[var_material.get()]))
    combo_material.grid(row=0, column = 2)
    #combo_material['values'] = data['city'].values.tolist()
    #combo_material.bind("<<ComboboxSelected>>", callback)
    label_selected = tk.Label(root, text="Not Selected")
    label_selected.grid(row=1, column=2)
    combo_material.current(0)
    tk.Label(root, text='Enter Mileage of your Bike/Car ',  bd=6).grid(row=3, column=0,pady=(3,3))
    spacer1 = tk.Label(root, text="")
    spacer1.grid(row=3, column=1)
    #name1 = tk.Label(root, text = '', font=('calibre',10, 'bold')).grid(row=3, column = 0)
    global name,name2
    name = tk.Entry(root,text=' ',width=25)
    name.grid(row=3, column = 2,sticky=W)
    name.bind("<Return>", on_change)
    tk.Label(root, text='(km/l)',bd=0.5).grid(row=3,column=3)

    tk.Label(root, text='Total number of km to be Travelled:',  bd=6).grid(row=4, column=0,pady=(3,3))
    name2 = tk.Entry(root,text=' ',width=25)
    name2.grid(row=4, column = 2,sticky=W)
    name2.bind("<Return>", on_change2)
    root.mainloop()



# class caluacaltion:

#     def __init__(self, url):
#         self.url = url

#     def __getdata__(self):
#         html = requests.get(url).content 
#         data = pd.read_html(html)[0]
#         return data



if __name__ == '__main__':

    dirname = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dirname)

    main()
    # url = 'https://economictimes.indiatimes.com/wealth/fuel-price/petrol'
    # data = caluacaltion(url).__getdata__()
    

    # print(data)
