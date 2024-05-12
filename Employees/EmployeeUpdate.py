import datetime
from tkinter import *
from tkinter import messagebox
from Database import Database

class EmployeeUpdate:
    def __init__(self, id):
        self.id = id
        self.main()

    #update method
    def update(self, tk, isim, soy_isim, tel_no, baslama_tarihi, maas, sube_id):

        try:
            db = Database()
            db.cursor.execute("UPDATE Calisanlar SET isim=?, soy_isim=?, tel_no=?, baslama_tarihi=?, maas=?, sube_id=? "
                              "WHERE sube_id=? ",
                              isim, soy_isim, tel_no, datetime.datetime.strptime(baslama_tarihi, "%Y-%m-%d %H:%M:%S.%f"),
                              maas, sube_id, self.id)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Çalışan başarıyla güncellendi")
            tk.destroy()


    def getData(self):
        db = Database()
        db.cursor.execute("SELECT * FROM Calisanlar WHERE calisan_id=?", self.id)
        self.data = db.cursor.fetchone()

    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ##  SELECT  ##
        self.getData()

        ###### update ######
        label_update = Label(tk, text="Çalışan Güncelle")
        label_update.grid(row=1, column=2)


        label_isim = Label(tk, text="İsim")
        label_isim.grid(row=2, column=1)
        update_isim = Entry(tk)
        update_isim.insert(0, self.data[1])
        update_isim.grid(row=2, column=2)

        label_soy_isim = Label(tk, text="Soy İsim")
        label_soy_isim.grid(row=3, column=1)
        update_soy_isim = Entry(tk)
        update_soy_isim.insert(0, self.data[2])
        update_soy_isim.grid(row=3, column=2)

        label_tel_no = Label(tk, text="Telefon Numarası")
        label_tel_no.grid(row=4, column=1)
        update_tel_no = Entry(tk)
        update_tel_no.insert(0, self.data[3])
        update_tel_no.grid(row=4, column=2)

        label_baslama_tarihi = Label(tk, text="Başlaama Tarihi")
        label_baslama_tarihi.grid(row=5, column=1)
        update_baslama_tarihi = Entry(tk)
        update_baslama_tarihi.insert(0, self.data[4])
        update_baslama_tarihi.grid(row=5, column=2)

        label_maas = Label(tk, text="Maaş")
        label_maas.grid(row=6, column=1)
        update_maas = Entry(tk)
        update_maas.insert(0, self.data[5])
        update_maas.grid(row=6, column=2)

        label_sube_id = Label(tk, text="Şube ID")
        label_sube_id.grid(row=7, column=1)
        update_sube_id = Entry(tk)
        update_sube_id.insert(0, self.data[6])
        update_sube_id.grid(row=7, column=2)

        btn_update = Button(tk,
                            text="Güncelle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.update(
                                tk,
                                update_isim.get(),
                                update_soy_isim.get(),
                                update_tel_no.get(),
                                update_baslama_tarihi.get(),
                                update_maas.get(),
                                update_sube_id.get()
                            ))
        btn_update.grid(row=11, column=2)