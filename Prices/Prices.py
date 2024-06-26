from tkinter import *
from tkinter import messagebox
from Database import Database
from Prices.PriceInsert import PriceInsert
from Prices.PriceUpdate import PriceUpdate
from generalQueries import *

class Prices:
    def __init__(self):
        self.main()


    def goInsert(self, tk):
        insert = PriceInsert()
        tk.destroy()


    def goUpdate(self, tk, id):
        update = PriceUpdate(id)
        tk.destroy()


    def deletePrice(self, tk, id):
        try:
            db = Database()
            db.cursor.execute("DELETE FROM Fiyatlar WHERE fiyat_id=?", id)
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
        db.cursor.execute("SELECT fiyat_id as 'ID', fiyat as 'Fiyatlar', max_agirlik as 'Maksimum Ağırlık' FROM Fiyatlar ")


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
                            text="Fiyat Ekle",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goInsert(tk))
        btn_insert.grid(row=i + 2, column=1)


        label_update = Label(tk, text="ID:")
        label_update.grid(row=i + 3, column=1)
        entry_update = Entry(tk)
        entry_update.grid(row=i + 3, column=2)
        btn_update = Button(tk,
                            text="Fiyat Güncelle",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goUpdate(tk, entry_update.get()))
        btn_update.grid(row=i + 3, column=3)

        label_delete = Label(tk, text="ID:")
        label_delete.grid(row=i + 4, column=1)
        entry_delete = Entry(tk)
        entry_delete.grid(row=i + 4, column=2)
        btn_delete = Button(tk,
                            text="Fiyat Sil",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.deletePrice(tk, entry_delete.get()))
        btn_delete.grid(row=i + 4, column=3)


        ### Row Count ###
        labelCount = Label(tk, text=f"Toplam Fiyat Paketi: {rowCount("Fiyatlar")}")
        labelCount.grid(row=i + 5, column=1)