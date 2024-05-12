from tkinter import *
from tkinter import messagebox
from Database import Database

class PriceInsert():
    def __init__(self):
        self.main()

    #insert method
    def insert(self,tk, fiyat, max_agirlik):

        try:
            db = Database()
            db.cursor.execute("INSERT INTO Fiyatlar (fiyat, max_agirlik) "
                              "VALUES (?, ?)",
                              fiyat, max_agirlik)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Fiyat başarıyla eklendi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ###### INSERT ######
        label_insert = Label(tk, text="Fiyat Ekle")
        label_insert.grid(row=1, column=2)

        label_fiyat = Label(tk, text="Fiyat")
        label_fiyat.grid(row=2, column=1)
        insert_fiyat = Entry(tk)
        insert_fiyat.grid(row=2, column=2)


        label_max_agirlik = Label(tk, text="Maximum Ağırlık")
        label_max_agirlik.grid(row=3, column=1)
        insert_max_agirlik = Entry(tk)
        insert_max_agirlik.grid(row=3, column=2)

        btn_insert = Button(tk,
                            text="Ekle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.insert(
                                tk,
                                insert_fiyat.get(),
                                insert_max_agirlik.get()
                            ))
        btn_insert.grid(row=10, column=2)
