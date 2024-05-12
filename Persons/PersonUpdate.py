from tkinter import *
from tkinter import messagebox
from Database import Database

class PersonUpdate():
    def __init__(self, id):
        self.id = id
        self.main()

    #update method
    def update(self, tk, isim, soy_isim, tel_no, adres_id):

        try:
            db = Database()
            db.cursor.execute("UPDATE Kisiler SET isim=?, soy_isim=?, tel_no=?, adres_id=? "
                              "WHERE kisi_id=?",
                              isim, soy_isim, tel_no, adres_id, self.id)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Kişi başarıyla güncellendi")
            tk.destroy()


    def getData(self):
        db = Database()
        db.cursor.execute("SELECT * FROM Kisiler WHERE kisi_id=?", self.id)
        self.data = db.cursor.fetchone()

    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ##  SELECT  ##
        self.getData()

        ###### update ######
        label_update = Label(tk, text="Kişi Güncelle")
        label_update.grid(row=1, column=2)


        label_isim = Label(tk, text="İsim")
        label_isim.grid(row=3, column=1)
        update_isim = Entry(tk)
        update_isim.insert(0, self.data[1])
        update_isim.grid(row=3, column=2)

        label_soy_isim = Label(tk, text="Soy İsim")
        label_soy_isim.grid(row=4, column=1)
        update_soy_isim = Entry(tk)
        update_soy_isim.insert(0, self.data[2])
        update_soy_isim.grid(row=4, column=2)

        label_tel_no = Label(tk, text="Telefon No")
        label_tel_no.grid(row=5, column=1)
        update_tel_no = Entry(tk)
        update_tel_no.insert(0, self.data[3])
        update_tel_no.grid(row=5, column=2)

        label_adres_id = Label(tk, text="Adres ID")
        label_adres_id.grid(row=6, column=1)
        update_adres_id = Entry(tk)
        update_adres_id.insert(0, self.data[4])
        update_adres_id.grid(row=6, column=2)


        btn_update = Button(tk,
                            text="Güncelle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.update(
                                tk,
                                update_isim.get(),
                                update_soy_isim.get(),
                                update_tel_no.get(),
                                update_adres_id.get()
                            ))
        btn_update.grid(row=11, column=2)