from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '2w4phKg5tR6LI2V5'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        query = request.form['query']

        conn = get_db_connection()
        conn.execute('INSERT INTO queries (query) VALUES (?)',
                        (query,)
        )
        conn.commit()
        conn.close()

    conn = get_db_connection()
    queries = conn.execute('SELECT * FROM queries').fetchall()
    conn.close()
    return render_template('index.html', queries=queries)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=2222)

