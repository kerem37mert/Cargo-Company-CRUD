from tkinter import *
from tkinter import messagebox
from Database import Database

class BrancUpdate():
    def __init__(self, id):
        self.id = id
        self.main()

    #update method
    def update(self, tk, adres_id, tel_no):

        try:
            db = Database()
            db.cursor.execute("UPDATE Subeler SET adres_id=?, tel_no=? WHERE sube_id=? ",
                              (adres_id, tel_no, self.id))
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Şube başarıyla güncellendi")
            tk.destroy()


    def getData(self):
        db = Database()
        db.cursor.execute("SELECT * FROM Subeler WHERE sube_id=?", self.id)
        self.data = db.cursor.fetchone()

    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ##  SELECT  ##
        self.getData()

        ###### update ######
        label_update = Label(tk, text="Şube Güncelle")
        label_update.grid(row=1, column=2)


        label_adres_id = Label(tk, text="Adres ID")
        label_adres_id.grid(row=3, column=1)
        update_adres_id = Entry(tk)
        update_adres_id.insert(0, self.data[1])
        update_adres_id.grid(row=3, column=2)


        label_tel_no = Label(tk, text="Telefon Numarası")
        label_tel_no.grid(row=4, column=1)
        update_tel_no = Entry(tk)
        update_tel_no.insert(0, self.data[2])
        update_tel_no.grid(row=4, column=2)


        btn_update = Button(tk,
                            text="Güncelle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.update(
                                tk,
                                update_adres_id.get(),
                                update_tel_no.get()
                            ))
        btn_update.grid(row=11, column=2)