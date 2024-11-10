import sqlite3
import os

DATABASE = '/data/database.db'

def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        );
    ''')

    conn.commit()
    conn.close()

def add_example_posts():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    example_posts = [
        ("Welcome to the Blog", "This is the first post on this blog."),
        ("Tips for Docker", "Here are some useful tips for using Docker effectively."),
        ("Getting Started with Flask", "This post introduces the basics of building a Flask app."),
    ]

    cursor.execute("SELECT COUNT(*) FROM posts;")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany('INSERT INTO posts (title, content) VALUES (?, ?)', example_posts)


    conn.commit()
    conn.close()

if __name__ == "__main__":
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)
    initialize_database()
    add_example_posts()
