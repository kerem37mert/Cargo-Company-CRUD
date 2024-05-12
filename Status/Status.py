from tkinter import *
from tkinter import messagebox
from Database import Database
from Status.StatusInsert import StatusInsert
from Status.StatusUpdate import StatusUpdate


class Status:
    def __init__(self, shipment_id):
        self.shipment_id = shipment_id
        self.main()


    def goInsert(self, tk):
        insert = StatusInsert(self.shipment_id)
        tk.destroy()


    def goUpdate(self, tk, id):
        update = StatusUpdate(id)
        tk.destroy()


    def deleteAddress(self, tk, id):
        try:
            db = Database()
            db.cursor.execute("DELETE FROM Durumlar WHERE durum_id=?", id)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", f"{id} ID'li satır başarıyla silindi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("1200x600")

        db = Database()
        db.cursor.execute("SELECT Durumlar.durum_id AS 'Durum ID', Durumlar.gonderi_id AS 'Gönderi ID', "
                          "Bilgiler.aciklama, Durumlar.tarih, Adresler.il, Adresler.ilce, Adresler.tam_adres "
                          "FROM Durumlar "
                          "LEFT JOIN Bilgiler ON bilgiler.bilgi_id = Durumlar.bilgi_id "
                          "LEFT JOIN Subeler ON Subeler.sube_id=Durumlar.sube_id "
                          "LEFT JOIN Adresler ON Adresler.adres_id=Subeler.adres_id "
                          "WHERE Durumlar.gonderi_id = ?", self.shipment_id)


        columns = [description[0] for description in db.cursor.description]
        for j, column_name in enumerate(columns):
            label = Label(tk, text=column_name)
            label.grid(row=0, column=j + 1)

        i = 1
        for row in db.cursor.fetchall():
            j = 1
            for cell in row:
                b = Entry(tk)
                b.insert(j, cell)
                b.grid(row=i, column=j)
                j += 1
                # print(str(cell))
            i += 1

        btn_insert = Button(tk,
                            text="Durum Ekle",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goInsert(tk))
        btn_insert.grid(row=i + 2, column=1)


        label_update = Label(tk, text="ID:")
        label_update.grid(row=i + 3, column=1)
        entry_update = Entry(tk)
        entry_update.grid(row=i + 3, column=2)
        btn_update = Button(tk,
                            text="Durum Güncelle",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goUpdate(tk, entry_update.get()))
        btn_update.grid(row=i + 3, column=3)

        label_delete = Label(tk, text="ID:")
        label_delete.grid(row=i + 4, column=1)
        entry_delete = Entry(tk)
        entry_delete.grid(row=i + 4, column=2)
        btn_delete = Button(tk,
                            text="Durum Sil",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.deleteAddress(tk, entry_delete.get()))
        btn_delete.grid(row=i + 4, column=3)
