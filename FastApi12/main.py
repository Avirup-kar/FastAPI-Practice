import sqlite3

conn = sqlite3.connect("test.db", check_same_thread = False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMERY KEY,
    title TEXT,
    completed TEXT
)
               """)