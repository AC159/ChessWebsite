import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


def get_conn():

    try:
        # For heroku:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode='require')

    except:
        conn = psycopg2.connect(dbname=os.getenv("DATABASE_NAME"), user=os.getenv("DATABASE_USER"),
                                password=os.getenv("DATABASE_PASSWORD"))

    return conn
