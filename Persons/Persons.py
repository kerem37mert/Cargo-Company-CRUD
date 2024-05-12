from tkinter import *
from tkinter import messagebox
from Database import Database
from Persons.PersonInsert import PersonInsert
from Persons.PersonUpdate import PersonUpdate


class Persons:
    def __init__(self):
        self.main()


    def goInsert(self, tk):
        insert = PersonInsert()
        tk.destroy()


    def goUpdate(self, tk, id):
        update = PersonUpdate(id)
        tk.destroy()


    def deleteAddress(self, tk, id):
        try:
            db = Database()
            db.cursor.execute("DELETE FROM Kisiler WHERE kisi_id=?", id)
            db.cnxn.commit()

        except:
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", f"{id} ID'li satır başarıyla silindi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("1200x600")

        db = Database()
        db.cursor.execute("SELECT Kisiler.kisi_id, Kisiler.isim, Kisiler.soy_isim, Kisiler.tel_no, "
                          "Adresler.il, Adresler.ilce, Adresler.posta_kodu, Adresler.tam_adres "
                          "FROM Kisiler "
                          "LEFT JOIN Adresler ON Kisiler.adres_id=Adresler.Adres_id ")


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
                            text="Kişi Ekle",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goInsert(tk))
        btn_insert.grid(row=i + 2, column=1)


        label_update = Label(tk, text="ID:")
        label_update.grid(row=i + 3, column=1)
        entry_update = Entry(tk)
        entry_update.grid(row=i + 3, column=2)
        btn_update = Button(tk,
                            text="Kişi Güncelle",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goUpdate(tk, entry_update.get()))
        btn_update.grid(row=i + 3, column=3)

        label_delete = Label(tk, text="ID:")
        label_delete.grid(row=i + 4, column=1)
        entry_delete = Entry(tk)
        entry_delete.grid(row=i + 4, column=2)
        btn_delete = Button(tk,
                            text="Kişi Sil",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.deleteAddress(tk, entry_delete.get()))
        btn_delete.grid(row=i + 4, column=3)
