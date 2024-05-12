from tkinter import *
from tkinter import messagebox
from Database import Database

class StatusUpdate:
    def __init__(self, id):
        self.id = id
        self.main()

    #update method
    def update(self, tk, bilgi_id, sube_id):

        try:
            db = Database()
            db.cursor.execute("UPDATE Durumlar SET bilgi_id=?, sube_id=? WHERE durum_id=?",
                              bilgi_id, sube_id, self.id)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Gönderi Durumu başarıyla güncellendi")
            tk.destroy()


    def getData(self):
        db = Database()
        db.cursor.execute("SELECT * FROM Durumlar WHERE durum_id=?", self.id)
        self.data = db.cursor.fetchone()

    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ##  SELECT  ##
        self.getData()

        ###### update ######
        label_update = Label(tk, text="Gönderi Durum Güncelle")
        label_update.grid(row=1, column=2)


        label_bilgi_id = Label(tk, text="Bilgi ID")
        label_bilgi_id.grid(row=3, column=1)
        update_bilgi_id = Entry(tk)
        update_bilgi_id.insert(0, self.data[2])
        update_bilgi_id.grid(row=3, column=2)


        label_sube_id = Label(tk, text="Şube ID")
        label_sube_id.grid(row=4, column=1)
        update_sube_id = Entry(tk)
        update_sube_id.insert(0, self.data[3])
        update_sube_id.grid(row=4, column=2)


        btn_update = Button(tk,
                            text="Güncelle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.update(
                                tk,
                                update_bilgi_id.get(),
                                update_sube_id.get(),
                            ))
        btn_update.grid(row=11, column=2)