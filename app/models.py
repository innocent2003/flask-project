import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

DB_HOST = 'localhost'
DB_NAME = 'crud_db'
DB_USER = 'postgres'
DB_PASSWORD = '123'

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

class User:
    @staticmethod
    def find_by_email(email):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, password FROM users WHERE email = %s', (email,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user

    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, name, email FROM users WHERE id = %s', (user_id,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user

    @staticmethod
    def all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, name, email FROM users')
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users

    @staticmethod
    def create(name, email, password):
        hashed_password = generate_password_hash(password, method='sha256')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
                    (name, email, hashed_password))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def update(user_id, name, email, password):
        hashed_password = generate_password_hash(password, method='sha256')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s',
                    (name, email, hashed_password, user_id))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete(user_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM users WHERE id = %s', (user_id,))
        conn.commit()
        cur.close()
        conn.close()
