from flask import Flask, jsonify, request, send_from_directory
import sqlite3

app = Flask(__name__, static_folder='static')

DATABASE = '/data/database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return jsonify([dict(post) for post in posts])

@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    title = new_post.get('title')
    content = new_post.get('content')

    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400
    
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()
    return jsonify({"message":"Post created successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)