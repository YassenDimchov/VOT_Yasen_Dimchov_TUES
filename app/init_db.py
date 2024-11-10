import sqlite3

connection = sqlite3.connect('database.db')

with open('init_db.sql') as file:
    connection.executescript(file.read())

connection.close()