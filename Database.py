import pyodbc

class Database:
    def __init__(self):
        self.cnxn = pyodbc.connect("Driver={SQL Server};"
                              r"Server=DESKTOP-SKM8I25\SQLEXPRESS;"
                              "Database=Cargo_Company;"
                              "Trusted_Connection=yes;")
        self.cursor = self.cnxn.cursor()