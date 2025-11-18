import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inventory_system"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()
        return self.cursor

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

db = Database()
