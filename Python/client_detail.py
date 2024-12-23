import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv('connection_string')

# print(connection_string)

connection=psycopg2.connect(connection_string)
cursor=connection.cursor()

# cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_catalog='fx';")

cursor.execute(f"SELECT * FROM logs;")
rows = cursor.fetchall()

# Fetch column names
column_names = [desc[0] for desc in cursor.description]

# Print column names
print(" | ".join(column_names))
print("-" * 50)

# Print each row of data
for row in rows:
    print(" | ".join(map(str, row)))


