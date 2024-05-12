from tkinter import *
from Address import Address

tk = Tk()
tk.title("Kargo Firması Veritabanı")
tk.geometry("1200x600")
Label(tk, text="Kargo Firması Veritabanı", font=25).pack()



#Go Address
def goAddress():
    address = Address()


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
btn_address.pack()


tk.mainloop()