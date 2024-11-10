from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return jsonify([dict(post) for post in posts])

@app.route('/posts', methods=['POSTS'])
def create_post():
    new_post = request.get_json()
    title = new_post.get('title')
    content = new_post.get('content')

    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400
    
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', title(title, content))
    conn.commit()
    conn.close()
    return jsonify({"message":{"Post created successfully"}}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)