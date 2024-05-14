from Database import Database

#### Row Count ####
def rowCount(tableName):
    db = Database()
    db.cursor.execute(f"SELECT COUNT(*) FROM {tableName}")
    return db.cursor.fetchone()[0]


#### Column Average ####
def columnAvg(columnName, tableName):
    db = Database()
    db.cursor.execute(f"SELECT AVG({columnName}) FROM {tableName}")
    return db.cursor.fetchone()[0]


#### Column Maximum ####
def columnMax(columnName, tableName):
    db = Database()
    db.cursor.execute(f"SELECT MAX({columnName}) FROM {tableName}")
    return db.cursor.fetchone()[0]


#### Column Minimum ####
def columnMax(columnName, tableName):
    db = Database()
    db.cursor.execute(f"SELECT MIN({columnName}) FROM {tableName}")
    return db.cursor.fetchone()[0]


#### Column Sum ####
def columnSum(columnName, tableName):
    db = Database()
    db.cursor.execute(f"SELECT SUM({columnName}) FROM {tableName}")
    return db.cursor.fetchone()[0]