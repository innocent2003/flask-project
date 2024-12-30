import psycopg2
from faker import Faker
from werkzeug.security import generate_password_hash

# Database connection details
DB_HOST = 'localhost'
DB_NAME = 'crud_db'
DB_USER = 'postgres'
DB_PASSWORD = '123'

# Function to get database connection
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

# Factory to generate fake data and insert it into the database
def generate_fake_users(num_rows=100):
    faker = Faker()
    conn = get_db_connection()
    cur = conn.cursor()

    for _ in range(num_rows):
        name = faker.name()
        email = faker.unique.email()
        password = generate_password_hash(faker.password(), method='sha256')

        # Insert the fake user into the database
        cur.execute(
            'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
            (name, email, password)
        )

    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {num_rows} fake users into the database.")

# Run the factory
if __name__ == '__main__':
    generate_fake_users(100)
