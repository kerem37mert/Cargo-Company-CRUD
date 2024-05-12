from tkinter import *
from tkinter import messagebox
from Database import Database

class InfoInsert:
    def __init__(self):
        self.main()

    #insert method
    def insert(self, tk, aciklama):

        try:
            db = Database()
            db.cursor.execute("INSERT INTO Bilgiler (aciklama) VALUES (?)",  aciklama)
            db.cnxn.commit()

        except Exception as e:
            print(e)
            messagebox.showinfo("Hata", "Bir sorun oluştu")
        else:
            messagebox.showinfo("Bilgi", "Gönderi Bilgisi başarıyla eklendi")
            tk.destroy()


    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        ###### INSERT ######
        label_insert = Label(tk, text="Gönderi Bilgisi Ekle")
        label_insert.grid(row=1, column=2)

        label_aciklama = Label(tk, text="Açıklama")
        label_aciklama.grid(row=2, column=1)
        insert_aciklama = Entry(tk)
        insert_aciklama.grid(row=2, column=2)


        btn_insert = Button(tk,
                            text="Ekle",
                            padx="10", pady="5",
                            cursor="hand2",
                            command=lambda: self.insert(
                                tk,
                                insert_aciklama.get()
                            ))
        btn_insert.grid(row=10, column=2)
