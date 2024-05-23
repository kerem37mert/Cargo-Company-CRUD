from tkinter import *
from tkinter import messagebox
from Database import Database

class AddressUpdate():
    def __init__(self, id):
        self.id = id
        self.main()

    #update method
    def update(self, tk, il, ilce, mah, cad, sokak, kapi_no, posta_kodu):

        try:
            db = Database()
            db.cursor.execute("UPDATE Adresler SET il=?, ilce=?, mah=?, cad=?, sokak=?, kapi_no=?, posta_kodu=? "
                              "WHERE adres_id=?",
                              il, ilce, mah, cad, sokak, kapi_no, posta_kodu, self.id)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Adres başarıyla güncellendi")
            tk.destroy()


    def getData(self):
        db = Database()
        db.cursor.execute("SELECT * FROM Adresler WHERE adres_id=?", self.id)
        self.data = db.cursor.fetchone()

    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ##  SELECT  ##
        self.getData()

        ###### update ######
        label_update = Label(tk, text="Adres Güncelle")
        label_update.grid(row=1, column=2)


        label_il = Label(tk, text="İl")
        label_il.grid(row=3, column=1)
        update_il = Entry(tk)
        update_il.insert(0, self.data[1])
        update_il.grid(row=3, column=2)

        label_ilce = Label(tk, text="ilçe")
        label_ilce.grid(row=4, column=1)
        update_ilce = Entry(tk)
        update_ilce.insert(0, self.data[2])
        update_ilce.grid(row=4, column=2)

        label_mah = Label(tk, text="mahalle")
        label_mah.grid(row=5, column=1)
        update_mah = Entry(tk)
        update_mah.insert(0, self.data[3])
        update_mah.grid(row=5, column=2)

        label_cad = Label(tk, text="Cadde")
        label_cad.grid(row=6, column=1)
        update_cad = Entry(tk)
        update_cad.insert(0, self.data[4])
        update_cad.grid(row=6, column=2)

        label_sokak = Label(tk, text="Sokak")
        label_sokak.grid(row=7, column=1)
        update_sokak = Entry(tk)
        update_sokak.insert(0, self.data[5])
        update_sokak.grid(row=7, column=2)

        label_kapi_no = Label(tk, text="Kapı No")
        label_kapi_no.grid(row=8, column=1)
        update_kapi_no = Entry(tk)
        update_kapi_no.insert(0, self.data[6])
        update_kapi_no.grid(row=8, column=2)

        label_posta_kodu = Label(tk, text="Posta Kodu")
        label_posta_kodu.grid(row=9, column=1)
        update_posta_kodu = Entry(tk)
        update_posta_kodu.insert(0, self.data[7])
        update_posta_kodu.grid(row=9, column=2)

        btn_update = Button(tk,
                            text="Güncelle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.update(
                                tk,
                                update_il.get(),
                                update_ilce.get(),
                                update_mah.get(),
                                update_cad.get(),
                                update_sokak.get(),
                                update_kapi_no.get(),
                                update_posta_kodu.get(),
                            ))
        btn_update.grid(row=11, column=2)