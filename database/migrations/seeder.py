from werkzeug.security import generate_password_hash
import psycopg2

# Database connection details
DB_HOST = 'localhost'
DB_NAME = 'crud_db'
DB_USER = 'postgres'
DB_PASSWORD = '123'

# Function to get database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# Seeder function to add initial users to the database
def seed_users():
    # Sample users data
    users = [
        {'name': 'Alice', 'email': 'alice@example.com', 'password': 'password123'},
        {'name': 'Bob', 'email': 'bob@example.com', 'password': 'password456'},
        {'name': 'Charlie', 'email': 'charlie@example.com', 'password': 'password789'}
    ]

    conn = get_db_connection()
    cur = conn.cursor()

    for user in users:
        hashed_password = generate_password_hash(user['password'], method='sha256')
        # Insert user data into the users table
        cur.execute(
            'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
            (user['name'], user['email'], hashed_password)
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Seeder has populated the users table.")

if __name__ == '__main__':
    seed_users()
