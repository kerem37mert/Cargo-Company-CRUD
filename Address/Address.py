from tkinter import *
from tkinter import messagebox
from Database import Database
from Address.AddressInsert import AddressInsert
from Address.AddressUpdate import AddressUpdate
from Address.Cities import Cities
from generalQueries import *

class Address:
    def __init__(self):
        self.main()


    def goInsert(self, tk):
        insert = AddressInsert()
        tk.destroy()


    def goCities(self, tk):
        cities = Cities()



    def goUpdate(self, tk, id):
        update = AddressUpdate(id)
        tk.destroy()

    def deleteAddress(self, tk, id):
        try:
            db = Database()
            db.cursor.execute("DELETE FROM Adresler WHERE adres_id=?", id)
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
        db.cursor.execute("EXEC SelectAllAddress")   ### Select all rows // Stored Procedure


        columns = [description[0] for description in db.cursor.description]
        for j, column_name in enumerate(columns):
            label = Label(tk, text=column_name)
            label.grid(row=0, column=j + 1)

        i =  1
        for row in db.cursor.fetchall():
            j = 1
            for cell in row:
                b = Entry(tk)
                b.insert(j, cell)
                b.grid(row=i, column=j)
                j += 1
                #print(str(cell))
            i += 1

        btn_insert = Button(tk,
                             text="Adres Ekle",
                             padx="20", pady="5",
                             cursor="hand2",
                             command=lambda: self.goInsert(tk))
        btn_insert.grid(row=i+2, column=1)


        btn_insert = Button(tk,
                            text="İlleri Göster",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goCities(tk))
        btn_insert.grid(row=i + 2, column=2)


        label_update = Label(tk, text="ID:")
        label_update.grid(row=i + 3, column=1)
        entry_update = Entry(tk)
        entry_update.grid(row=i + 3, column=2)
        btn_update = Button(tk,
                            text="Adres Güncelle",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goUpdate(tk, entry_update.get()))
        btn_update.grid(row=i + 3, column=3)


        label_delete = Label(tk, text="ID:")
        label_delete.grid(row=i+4, column=1)
        entry_delete = Entry(tk)
        entry_delete.grid(row=i+4, column=2)
        btn_delete = Button(tk,
                            text="Adres Sil",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.deleteAddress(tk, entry_delete.get()))
        btn_delete.grid(row=i+4, column=3)

        ### Row Count ###
        labelCount = Label(tk, text=f"Toplam Adres Sayısı: {rowCount("Adresler")}")
        labelCount.grid(row=i+5, column=1)


