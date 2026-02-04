import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="hospital_db",
        user="postgres",
        password="YOUR_POSTGRES_PASSWORD",
        port="5432"
    )
