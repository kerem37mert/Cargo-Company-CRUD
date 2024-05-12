from tkinter import *
from tkinter import messagebox
from Database import Database

class StatusInsert:
    def __init__(self, shipment_id):
        self.shipment_id = shipment_id
        self.main()

    #insert method
    def insert(self, tk, bilgi_id, sube_id):

        try:
            db = Database()
            db.cursor.execute("INSERT INTO Durumlar (gonderi_id, bilgi_id, sube_id) "
                              " VALUES (?, ?, ?)",
                              self.shipment_id, bilgi_id, sube_id)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Gönderi Durumu başarıyla eklendi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ###### INSERT ######
        label_insert = Label(tk, text="Gönderi Durumu Ekle")
        label_insert.grid(row=1, column=2)

        label_bilgi_id = Label(tk, text="Bilgi ID")
        label_bilgi_id.grid(row=2, column=1)
        insert_bilgi_id = Entry(tk)
        insert_bilgi_id.grid(row=2, column=2)

        label_sube_id = Label(tk, text="Şube ID")
        label_sube_id.grid(row=3, column=1)
        insert_sube_id = Entry(tk)
        insert_sube_id.grid(row=3, column=2)


        btn_insert = Button(tk,
                            text="Ekle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.insert(
                                tk,
                                insert_bilgi_id.get(),
                                insert_sube_id.get()
                            ))
        btn_insert.grid(row=10, column=2)
