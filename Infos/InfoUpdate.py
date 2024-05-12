import datetime
from tkinter import *
from tkinter import messagebox
from Database import Database

class InfoUpdate:
    def __init__(self, id):
        self.id = id
        self.main()

    #update method
    def update(self, tk, aciklama):

        try:
            db = Database()
            db.cursor.execute("UPDATE Bilgiler SET aciklama=? WHERE bilgi_id=?", aciklama, self.id)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Gönderi Bilgisi başarıyla güncellendi")
            tk.destroy()


    def getData(self):
        db = Database()
        db.cursor.execute("SELECT * FROM Bilgiler WHERE bilgi_id=?", self.id)
        self.data = db.cursor.fetchone()

    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ##  SELECT  ##
        self.getData()

        ###### update ######
        label_update = Label(tk, text="Çalışan Güncelle")
        label_update.grid(row=1, column=2)


        label_aciklama = Label(tk, text="Açıklama")
        label_aciklama.grid(row=2, column=1)
        update_aciklama = Entry(tk)
        update_aciklama.insert(0, self.data[1])
        update_aciklama.grid(row=2, column=2)


        btn_update = Button(tk,
                            text="Güncelle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.update(
                                tk,
                                update_aciklama.get()
                            ))
        btn_update.grid(row=11, column=2)