from tkinter import *
from tkinter import messagebox
from Database import Database

class BranchInsert:
    def __init__(self):
        self.main()

    #insert method
    def insert(self,tk, adres_id, tel_no):

        try:
            db = Database()
            db.cursor.execute("INSERT INTO Subeler (adres_id, tel_no) "
                              "VALUES (?, ?)",
                              (adres_id, tel_no))
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Şube başarıyla eklendi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ###### INSERT ######
        label_insert = Label(tk, text="Şube Ekle")
        label_insert.grid(row=1, column=2)

        label_adres_id = Label(tk, text="Adres ID")
        label_adres_id.grid(row=2, column=1)
        insert_adres_id = Entry(tk)
        insert_adres_id.grid(row=2, column=2)


        label_tel_no = Label(tk, text="Telefon No")
        label_tel_no.grid(row=3, column=1)
        insert_tel_no = Entry(tk)
        insert_tel_no.grid(row=3, column=2)


        btn_insert = Button(tk,
                            text="Ekle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.insert(
                                tk,
                                insert_adres_id.get(),
                                insert_tel_no.get()
                            ))
        btn_insert.grid(row=10, column=2)
