import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY, username, password)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM login")
        rows = self.cur.fetchall()
        return rows

    def insert(self, username, password):
        self.cur.execute("INSERT INTO login VALUES (NULL, ?, ?)",
                         (username, password))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM login WHERE id=?", (id,))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()

