import pymysql
import os
from dotenv import load_dotenv
from pathlib import Path

# Load env variables
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# Database connection details from .env
connection = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT")),
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Read the SQL file
        with open('campus.sql', 'r', encoding='utf-8') as f:
            sql_file = f.read()
        
        # Split by semicolon to execute one by one
        sql_commands = sql_file.split(';')
        for command in sql_commands:
            if command.strip():
                try:
                    cursor.execute(command)
                except Exception as e:
                    print(f"Skipping error: {e}")
        
    connection.commit()
    print("Data import successful!")
finally:
    connection.close()