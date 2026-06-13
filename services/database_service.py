import sqlite3

from config import DATABASE_PATH


class DatabaseService:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE_PATH)

        self.create_table()

    def create_table(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_analysis
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            ticker TEXT,

            current_price REAL,

            roe REAL,

            debt_equity REAL,

            buffett_score REAL
        )
        """)

        self.conn.commit()

    def save(self,
             ticker,
             current_price,
             roe,
             debt_equity,
             buffett_score):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO stock_analysis
        (
            ticker,
            current_price,
            roe,
            debt_equity,
            buffett_score
        )
        VALUES
        (
            ?,?,?,?,?
        )
        """,
                       (
                           ticker,
                           current_price,
                           roe,
                           debt_equity,
                           buffett_score
                       ))

        self.conn.commit()