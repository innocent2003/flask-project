import os
import psycopg2
from psycopg2 import sql

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

# Migration folder path
MIGRATION_FOLDER = 'migrations/versions/'

# Function to apply a migration
def apply_migration(migration_file):
    with open(migration_file, 'r') as file:
        migration_sql = file.read()

    conn = get_db_connection()
    cur = conn.cursor()

    # Execute the migration SQL
    cur.execute(migration_sql)
    conn.commit()

    cur.close()
    conn.close()

# Function to generate a new migration file
def create_migration(name):
    migration_file = os.path.join(MIGRATION_FOLDER, f'{name}.sql')
    if not os.path.exists(MIGRATION_FOLDER):
        os.makedirs(MIGRATION_FOLDER)

    # Create a basic migration template
    with open(migration_file, 'w') as file:
        file.write('-- Write your SQL migration here\n')
        file.write('-- Example: CREATE TABLE admins (id SERIAL PRIMARY KEY, name VARCHAR(100));\n')

    print(f"Migration file created: {migration_file}")
