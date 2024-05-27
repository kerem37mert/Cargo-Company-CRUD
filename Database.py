import pyodbc

class Database:
    def __init__(self):
        try:

            # SQL Server
            self.cnxn = pyodbc.connect("Driver={SQL Server};"
                                       r"Server=DESKTOP-SKM8I25\SQLEXPRESS;"
                                       "Database=Cargo_Company;"
                                       "Trusted_Connection=yes;")

        except Exception as e:
            print(f"Error: {e}")
        else:
            self.cursor = self.cnxn.cursor()