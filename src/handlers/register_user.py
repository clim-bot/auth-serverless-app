import json
import psycopg2
from config import POSTGRES_HOST, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD

def lambda_handler(event, context):
    user_data = json.loads(event['body'])
    username = user_data['username']
    password = user_data['password']

    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cur.close()
    conn.close()

    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'User registered successfully'})
    }
