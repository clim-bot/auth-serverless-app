import psycopg2
from config import POSTGRES_HOST, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD

def populate_db():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        );
    """)

    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", ("user1", "password1"))
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", ("user2", "password2"))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    populate_db()
