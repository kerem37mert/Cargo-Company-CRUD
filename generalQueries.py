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

