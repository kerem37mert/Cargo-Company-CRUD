from tkinter import *
from tkinter import messagebox
from Database import Database

class ShipmentUpdate():
    def __init__(self, id):
        self.id = id
        self.main()

    #update method
    def update(self, tk, gonderici_id, alici_id, agirlik):

        try:
            db = Database()
            db.cursor.execute("UPDATE Gonderiler SET gonderici_id=?, alici_id=?, agirlik=?, "
                              "fiyat_id=(SELECT TOP(1) fiyat_id FROM Fiyatlar WHERE ? <= max_agirlik ORDER BY max_agirlik ASC) "
                              "WHERE gonderi_id=?",
                              gonderici_id, alici_id, agirlik, agirlik, self.id)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Gönderi başarıyla güncellendi")
            tk.destroy()


    def getData(self):
        db = Database()
        db.cursor.execute("SELECT * FROM GOnderiler WHERE gonderi_id=?", self.id)
        self.data = db.cursor.fetchone()

    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ##  SELECT  ##
        self.getData()

        ###### update ######
        label_update = Label(tk, text="Fiyat Güncelle")
        label_update.grid(row=1, column=2)


        label_gonderici_id = Label(tk, text="Gönderici ID")
        label_gonderici_id.grid(row=3, column=1)
        update_gonderici_id = Entry(tk)
        update_gonderici_id.insert(0, self.data[1])
        update_gonderici_id.grid(row=3, column=2)


        label_alici_id = Label(tk, text="Alıcı ID")
        label_alici_id.grid(row=4, column=1)
        update_alici_id = Entry(tk)
        update_alici_id.insert(0, self.data[2])
        update_alici_id.grid(row=4, column=2)


        label_agirlik = Label(tk, text="Ağırlık")
        label_agirlik.grid(row=5, column=1)
        update_agirlik = Entry(tk)
        update_agirlik.insert(0, self.data[4])
        update_agirlik.grid(row=5, column=2)


        btn_update = Button(tk,
                            text="Güncelle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.update(
                                tk,
                                update_gonderici_id.get(),
                                update_alici_id.get(),
                                update_agirlik.get()
                            ))
        btn_update.grid(row=11, column=2)