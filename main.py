from tkinter import *
from Address.Address import Address
from Persons.Persons import Persons
from Prices.Prices import Prices
from Shipments.Shipments import Shipments
from Branches.Branches import Branches
from Employees.Employees import Employees

tk = Tk()
tk.title("Kargo Firması Veritabanı")
tk.geometry("1200x600")
Label(tk, text="Kargo Firması Veritabanı", font=25).pack()



#Go Address
def goAddress():
    address = Address()

def goPersons():
    persons = Persons()

def goPrices():
    prices = Prices()

def goShipments():
    shipments = Shipments()

def goBranches():
    branches = Branches()

def goEmployees():
    employees = Employees()


btn_address = Button(tk,
            text="Adresler",
            padx="20",pady="5",
            cursor="hand2",
            command=goAddress)
btn_address.pack()


btn_kisiler = Button(tk,
            text="Kişiler",
            padx="20",pady="5",
            cursor="hand2",
            command=goPersons)
btn_kisiler.pack()


btn_fiyatlar = Button(tk,
            text="Fiyatlar",
            padx="20",pady="5",
            cursor="hand2",
            command=goPrices)
btn_fiyatlar.pack()


btn_gonderiler = Button(tk,
            text="Gönderiler",
            padx="20",pady="5",
            cursor="hand2",
            command=goShipments)
btn_gonderiler.pack()


btn_subeler = Button(tk,
            text="Şubeler",
            padx="20",pady="5",
            cursor="hand2",
            command=goBranches)
btn_subeler.pack()


btn_subeler = Button(tk,
            text="Çalışanlar",
            padx="20",pady="5",
            cursor="hand2",
            command=goEmployees)
btn_subeler.pack()

tk.mainloop()