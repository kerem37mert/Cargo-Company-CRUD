from tkinter import *
from tkinter import messagebox
from Database import Database
from Employees.EmployeeInsert import EmployeeInsert
from Employees.EmployeeUpdate import EmployeeUpdate
from generalQueries import *


class Employees:
    def __init__(self):
        self.main()


    def goInsert(self, tk):
        insert = EmployeeInsert()
        tk.destroy()


    def goUpdate(self, tk, id):
        update = EmployeeUpdate(id)
        tk.destroy()


    def deleteEmployee(self, tk, id):
        try:
            db = Database()
            db.cursor.execute("DELETE FROM Calisanlar WHERE calisan_id=?", id)
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
        db.cursor.execute("SELECT Calisanlar.calisan_id AS 'ID', Calisanlar.isim AS 'İsim', "
                          "Calisanlar.soy_isim AS 'Soy İsim', "
                          "Calisanlar.tel_no AS 'Telefon NO', Calisanlar.baslama_tarihi AS 'Başlama tarihi', "
                          "Calisanlar.maas, Subeler.sube_id, Subeler.adres_id AS 'Şube Adres ID' "
                          "FROM Calisanlar "
                          "LEFT JOIN Subeler ON Subeler.sube_id=Calisanlar.sube_id ")


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
                            text="Çalışan Ekle",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goInsert(tk))
        btn_insert.grid(row=i + 2, column=1)


        label_update = Label(tk, text="ID:")
        label_update.grid(row=i + 3, column=1)
        entry_update = Entry(tk)
        entry_update.grid(row=i + 3, column=2)
        btn_update = Button(tk,
                            text="Çalışan Güncelle",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.goUpdate(tk, entry_update.get()))
        btn_update.grid(row=i + 3, column=3)

        label_delete = Label(tk, text="ID:")
        label_delete.grid(row=i + 4, column=1)
        entry_delete = Entry(tk)
        entry_delete.grid(row=i + 4, column=2)
        btn_delete = Button(tk,
                            text="Çalışan Sil",
                            padx="20", pady="5",
                            cursor="hand2",
                            command=lambda: self.deleteEmployee(tk, entry_delete.get()))
        btn_delete.grid(row=i + 4, column=3)

        ### Row Count ###
        labelCount = Label(tk, text=f"Toplam Çalışan Sayısı: {rowCount("Calisanlar")}")
        labelCount.grid(row=i + 5, column=1)
