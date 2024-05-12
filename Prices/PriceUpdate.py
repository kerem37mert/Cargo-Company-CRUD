from tkinter import *
from tkinter import messagebox
from Database import Database

class PriceUpdate():
    def __init__(self, id):
        self.id = id
        self.main()

    #update method
    def update(self, tk, fiyat, max_agirlik):

        try:
            db = Database()
            db.cursor.execute("UPDATE Fiyatlar SET fiyat=?, max_agirlik=? "
                              "WHERE fiyat_id=?",
                              fiyat, max_agirlik, self.id)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Fiyat başarıyla güncellendi")
            tk.destroy()


    def getData(self):
        db = Database()
        db.cursor.execute("SELECT * FROM Fiyatlar WHERE fiyat_id=?", self.id)
        self.data = db.cursor.fetchone()

    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ##  SELECT  ##
        self.getData()

        ###### update ######
        label_update = Label(tk, text="Fiyat Güncelle")
        label_update.grid(row=1, column=2)


        label_fiyat = Label(tk, text="Fiyat")
        label_fiyat.grid(row=3, column=1)
        update_fiyat = Entry(tk)
        update_fiyat.insert(0, self.data[1])
        update_fiyat.grid(row=3, column=2)

        label_max_agirlik = Label(tk, text="Maksimum Ağırlık")
        label_max_agirlik.grid(row=4, column=1)
        update_max_agirlik = Entry(tk)
        update_max_agirlik.insert(0, self.data[2])
        update_max_agirlik.grid(row=4, column=2)


        btn_update = Button(tk,
                            text="Güncelle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.update(
                                tk,
                                update_fiyat.get(),
                                update_max_agirlik.get()
                            ))
        btn_update.grid(row=11, column=2)