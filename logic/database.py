import sqlite3
import os


DATABASE_PATH = 'promo.db'


def init_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Check if the tables already exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_promo_data'")
    user_data_table_exists = cursor.fetchone()

    # Create the 'user_data' table if it doesn't exist
    if not user_data_table_exists:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_promo_data (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

    conn.commit()
    conn.close()

# Call init_database to create tables if they don't exist
init_database()

def store_user_data(name, email):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO user_promo_data (name, email)
        VALUES (?, ?)
    ''', (name, email))

    conn.commit()
    conn.close()


def fetch_user_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM user_promo_data')
    user_data = cursor.fetchall()

    conn.close()
    return user_data

