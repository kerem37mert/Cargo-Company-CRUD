from tkinter import *
from tkinter import messagebox
from Database import Database

class PersonInsert():
    def __init__(self):
        self.main()

    #insert method
    def insert(self,tk, isim, soy_isim, tel_no, adres_id):

        try:
            db = Database()
            db.cursor.execute("INSERT INTO Kisiler (isim, soy_isim, tel_no, adres_id) "
                              "VALUES (?, ?, ? ,?)",
                              isim, soy_isim, tel_no, adres_id)
            db.cnxn.commit()

        except:
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Kişi başarıyla eklendi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ###### INSERT ######
        label_insert = Label(tk, text="Kişi Ekle")
        label_insert.grid(row=1, column=2)

        label_isim = Label(tk, text="İsim")
        label_isim.grid(row=2, column=1)
        insert_isim = Entry(tk)
        insert_isim.grid(row=2, column=2)

        label_soy_isim = Label(tk, text="Soy İsim")
        label_soy_isim.grid(row=3, column=1)
        insert_soy_isim = Entry(tk)
        insert_soy_isim.grid(row=3, column=2)

        label_tel_no = Label(tk, text="Telefon No")
        label_tel_no.grid(row=4, column=1)
        insert_tel_no = Entry(tk)
        insert_tel_no.grid(row=4, column=2)

        label_adres_id = Label(tk, text="Adres ID")
        label_adres_id.grid(row=5, column=1)
        insert_adres_id = Entry(tk)
        insert_adres_id.grid(row=5, column=2)


        btn_insert = Button(tk,
                            text="Ekle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.insert(
                                tk,
                                insert_isim.get(),
                                insert_soy_isim.get(),
                                insert_tel_no.get(),
                                insert_adres_id.get(),
                            ))
        btn_insert.grid(row=10, column=2)
