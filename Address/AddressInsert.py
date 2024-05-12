from tkinter import *
from tkinter import messagebox
from Database import Database

class AddressInsert():
    def __init__(self):
        self.main()

    #insert method
    def insert(self,tk, il, ilce, mah, cad, sokak, kapi_no, posta_kodu, tam_adres):

        try:
            db = Database()
            db.cursor.execute("INSERT INTO Adresler (il, ilce, mah, cad, sokak, kapi_no, posta_kodu, tam_adres)"
                              "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",

                              il, ilce, mah, cad, sokak, kapi_no, posta_kodu, tam_adres)
            db.cnxn.commit()

        except:
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Adres başarıyla eklendi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ###### INSERT ######
        label_insert = Label(tk, text="Adres Ekle")
        label_insert.grid(row=1, column=2)

        label_il = Label(tk, text="İl")
        label_il.grid(row=2, column=1)
        insert_il = Entry(tk)
        insert_il.grid(row=2, column=2)

        label_ilce = Label(tk, text="ilçe")
        label_ilce.grid(row=3, column=1)
        insert_ilce = Entry(tk)
        insert_ilce.grid(row=3, column=2)

        label_mah = Label(tk, text="mahalle")
        label_mah.grid(row=4, column=1)
        insert_mah = Entry(tk)
        insert_mah.grid(row=4, column=2)

        label_cad = Label(tk, text="Cadde")
        label_cad.grid(row=5, column=1)
        insert_cad = Entry(tk)
        insert_cad.grid(row=5, column=2)

        label_sokak = Label(tk, text="Sokak")
        label_sokak.grid(row=6, column=1)
        insert_sokak = Entry(tk)
        insert_sokak.grid(row=6, column=2)

        label_kapi_no = Label(tk, text="Kapı No")
        label_kapi_no.grid(row=7, column=1)
        insert_kapi_no = Entry(tk)
        insert_kapi_no.grid(row=7, column=2)

        label_posta_kodu = Label(tk, text="Posta Kodu")
        label_posta_kodu.grid(row=8, column=1)
        insert_posta_kodu = Entry(tk)
        insert_posta_kodu.grid(row=8, column=2)

        label_tam_adres = Label(tk, text="Tam Adres")
        label_tam_adres.grid(row=9, column=1)
        insert_tam_adres = Entry(tk)
        insert_tam_adres.grid(row=9, column=2)

        btn_insert = Button(tk,
                            text="Ekle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.insert(
                                tk,
                                insert_il.get(),
                                insert_ilce.get(),
                                insert_mah.get(),
                                insert_cad.get(),
                                insert_sokak.get(),
                                insert_kapi_no.get(),
                                insert_posta_kodu.get(),
                                insert_tam_adres.get()
                            ))
        btn_insert.grid(row=10, column=2)