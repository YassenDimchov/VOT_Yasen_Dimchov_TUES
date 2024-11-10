import sqlite3

connection = sqlite3.connect('database.db')

def add_post(title, content):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()

with open('init_db.sql') as file:
    connection.executescript(file.read())
    
add_post("First Post", "This is the content of the first post")
add_post("Second Post", "This is the content of the second post")
connection.close()

