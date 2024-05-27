from tkinter import *
from Database import Database


class PersonSearch:
    def __init__(self, query):
        self.query = query
        self.main()

    def main(self):
        tk = Tk()
        tk.geometry("800x400")

        db = Database()
        db.cursor.execute("SELECT TOP 10 * FROM KisiKisaBilgi "
                          "WHERE isim LIKE ? OR soy_isim LIKE ? "
                          "ORDER BY isim ASC",
                          f"%{self.query}%", f"%{self.query}%")

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