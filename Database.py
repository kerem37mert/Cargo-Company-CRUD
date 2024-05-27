import pyodbc

class Database:
    def __init__(self):
        try:

            #SQL Server
            self.cnxn = pyodbc.connect("Driver={SQL Server};"
                                       r"Server=DESKTOP-SKM8I25\SQLEXPRESS;"
                                       "Database=Cargo_Company;"
                                       "Trusted_Connection=yes;")


            #POSTGRESQL
            # conn_str = (
            #     "Driver={PostgreSQL Unicode};"
            #     "Server=localhost;"
            #     "Port=5432;"
            #     "Database=cargo_company;"
            #     "Uid=postgres;"
            #     "Pwd=my_password;"         # Password input
            # )
            # self.cnxn = pyodbc.connect(conn_str)

            print("connected to database")

        except Exception as e:
            print(f"Error: {e}")
        else:
            self.cursor = self.cnxn.cursor()
