from tkinter import *
from tkinter import messagebox
from Database import Database

class ShipmentInsert:
    def __init__(self):
        self.main()

    #insert method
    def insert(self,tk, gonderici_id, alici_id, agirlik):

        try:
            db = Database()
            db.cursor.execute("INSERT INTO Gonderiler (gonderici_id, alici_id, agirlik, fiyat_id) "
                              "VALUES (?, ?, ?, "
                              "(SELECT TOP(1) fiyat_id FROM Fiyatlar WHERE ? <= max_agirlik ORDER BY max_agirlik ASC))",
                              gonderici_id, alici_id, agirlik, agirlik)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Gönderi başarıyla eklendi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ###### INSERT ######
        label_insert = Label(tk, text="Gönderi Ekle")
        label_insert.grid(row=1, column=2)

        label_gonderici_id = Label(tk, text="Gönderici ID")
        label_gonderici_id.grid(row=2, column=1)
        insert_gonderici_id = Entry(tk)
        insert_gonderici_id.grid(row=2, column=2)


        label_alici_id = Label(tk, text="Alıcı ID")
        label_alici_id.grid(row=3, column=1)
        insert_alici_id= Entry(tk)
        insert_alici_id.grid(row=3, column=2)


        label_agirlik = Label(tk, text="Ağırlık")
        label_agirlik.grid(row=4, column=1)
        insert_agirlik = Entry(tk)
        insert_agirlik.grid(row=4, column=2)


        btn_insert = Button(tk,
                            text="Ekle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.insert(
                                tk,
                                insert_gonderici_id.get(),
                                insert_alici_id.get(),
                                insert_agirlik.get()
                            ))
        btn_insert.grid(row=10, column=2)
