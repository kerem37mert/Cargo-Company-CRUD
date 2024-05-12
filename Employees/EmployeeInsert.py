from tkinter import *
from tkinter import messagebox
from Database import Database

class EmployeeInsert:
    def __init__(self):
        self.main()

    #insert method
    def insert(self,tk, isim, soy_isim, tel_no, maas, sube_id):

        try:
            db = Database()
            db.cursor.execute("INSERT INTO Calisanlar (isim, soy_isim, tel_no, maas, sube_id) "
                              "VALUES (?, ?, ?, ?, ?)",
                              (isim, soy_isim, tel_no, maas, sube_id))
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Çalışan başarıyla eklendi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ###### INSERT ######
        label_insert = Label(tk, text="Çalışan Ekle")
        label_insert.grid(row=1, column=2)

        label_isim = Label(tk, text="İsim")
        label_isim.grid(row=2, column=1)
        insert_isim= Entry(tk)
        insert_isim.grid(row=2, column=2)

        label_soy_isim = Label(tk, text="Soy İsim")
        label_soy_isim.grid(row=3, column=1)
        insert_soy_isim = Entry(tk)
        insert_soy_isim.grid(row=3, column=2)

        label_tel_no = Label(tk, text="Telefon No")
        label_tel_no.grid(row=4, column=1)
        insert_tel_no = Entry(tk)
        insert_tel_no.grid(row=4, column=2)

        label_maas = Label(tk, text="Maaş")
        label_maas.grid(row=6, column=1)
        insert_maas = Entry(tk)
        insert_maas.grid(row=6, column=2)

        label_sube_id = Label(tk, text="Şube ID")
        label_sube_id.grid(row=7, column=1)
        insert_sube_id = Entry(tk)
        insert_sube_id.grid(row=7, column=2)


        btn_insert = Button(tk,
                            text="Ekle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.insert(
                                tk,
                                insert_isim.get(),
                                insert_soy_isim.get(),
                                insert_tel_no.get(),
                                insert_maas.get(),
                                insert_sube_id.get()
                            ))
        btn_insert.grid(row=10, column=2)
