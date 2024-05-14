from Database import Database

#### Row Count ####
def rowCount(tableName):
    db = Database()
    db.cursor.execute(f"SELECT COUNT(*) FROM {tableName}")
    return db.cursor.fetchone()[0]

