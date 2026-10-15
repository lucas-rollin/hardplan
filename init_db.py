"""SQlite database initialization script."""

import sqlite3

SCHEMA_FILE = 'static/tables.sql'
DB_FILE = 'database.db'

with open(SCHEMA_FILE, 'r', encoding='utf-8') as file:
    schema_sql = file.read()

with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.executescript(schema_sql)
    conn.commit()

print(f"Initialized the database successfully!")
