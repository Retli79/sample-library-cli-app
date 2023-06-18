import psycopg2
from psycopg2 import Error

def connect():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database="Group2DB"
        )
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

