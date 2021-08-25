import sqlite3

connection = sqlite3.connect('app.db')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL UNIQUE,
password TEXT NOT NULL,
fname TEXT NOT NULL,
lname TEXT NOT NULL
);


    """)

