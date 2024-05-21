from tkinter import *
from Database import Database


class Cities:
    def __init__(self):
        self.main()

    def main(self):
        tk = Tk()
        tk.geometry("400x400")

        db = Database()
        db.cursor.execute("SELECT il, COUNT(il) AS 'Sayı' FROM Adresler GROUP BY il ORDER BY COUNT(il) DESC")

        columns = [description[0] for description in db.cursor.description]
        for j, column_name in enumerate(columns):
            label = Label(tk, text=column_name)
            label.grid(row=0, column=j + 1)

        i = 1
        for row in db.cursor.fetchall():
            j = 1
            for cell in row:
                b = Entry(tk)
                b.insert(j, cell)
                b.grid(row=i, column=j)
                j += 1
                # print(str(cell))
            i += 1