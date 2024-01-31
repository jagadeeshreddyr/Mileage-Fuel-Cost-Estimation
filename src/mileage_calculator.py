import tkinter as tk
from tkinter import ttk
import requests 
import pandas as pd

class MileageCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Mileage Calculator")

        self.url = 'https://economictimes.indiatimes.com/wealth/fuel-price/petrol'
        self.html = requests.get(self.url).content 

        data = pd.read_html(self.html)[0]
        self.prices = dict(zip(data['city'], data['Petrol Price']))

        # Style configuration
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        style.configure('TButton', background='#4CAF50', foreground='white', padding=(10, 5))
        style.configure('TCombobox', background='white')

        # Frame
        self.main_frame = ttk.Frame(master, padding=(20, 10))
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Dropdown menu for selecting city
        self.city_label = ttk.Label(self.main_frame, text="Select City:")
        self.city_label.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
        self.city_var = tk.StringVar(master)
        self.city_var.set(list(self.prices.keys())[0])  # Set the default city
        self.city_combobox = ttk.Combobox(self.main_frame, textvariable=self.city_var, values=list(self.prices.keys()), state="readonly")
        self.city_combobox.grid(row=0, column=1, pady=10, padx=10)
        self.city_combobox.bind("<<ComboboxSelected>>", lambda event: self.update_price())

        # Label to display the fuel price
        self.price_label = ttk.Label(self.main_frame, text="Price: ₹0")
        self.price_label.grid(row=0, column=2, pady=10, padx=10)

        # Entry widget for inputting total quantity in liters
        self.quantity_label = ttk.Label(self.main_frame, text="Total Quantity in liters:")
        self.quantity_label.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)
        self.quantity_entry = ttk.Entry(self.main_frame)
        self.quantity_entry.grid(row=1, column=1, pady=10, padx=10)

        # Entry widget for inputting total distance traveled
        self.distance_label = ttk.Label(self.main_frame, text="Total km traveled:")
        self.distance_label.grid(row=2, column=0, pady=10, padx=10, sticky=tk.W)
        self.distance_entry = ttk.Entry(self.main_frame)
        self.distance_entry.grid(row=2, column=1, pady=10, padx=10)

        # Button to calculate and display the mileage and total cost
        self.calculate_button = ttk.Button(self.main_frame, text="Calculate Mileage", command=self.calculate_mileage)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Label to display the calculated mileage
        self.result_label = ttk.Label(self.main_frame, text="Mileage: km/l", font=('Arial', 14, 'bold'))
        self.result_label.grid(row=5, column=0, columnspan=3, pady=10)

        # Label to display the total cost
        self.total_cost_label = ttk.Label(self.main_frame, text="Total Cost: ₹", font=('Arial', 14, 'bold'))
        self.total_cost_label.grid(row=6, column=0, columnspan=3, pady=10)

    def update_price(self):
        selected_city = self.city_var.get()
        price = self.prices.get(selected_city, 0)
        self.price_label.config(text=f"Price: ₹{price}")

    def calculate_mileage(self):
        selected_city = self.city_var.get()
        quantity = float(self.quantity_entry.get())
        distance = float(self.distance_entry.get())

        # Replace this with your own logic to calculate the mileage based on the selected city, quantity, and distance
        mileage = distance / quantity if quantity != 0 else 0
        total_cost = float(self.prices[selected_city].split('₹')[0]) * quantity

        self.result_label.config(text=f'Mileage: {mileage:.2f} km/l')
        self.total_cost_label.config(text=f'Total Cost: ₹{total_cost:.2f}')

if __name__ == "__main__":
    root = tk.Tk()
    app = MileageCalculator(root)
    root.mainloop()
