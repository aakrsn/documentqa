# database functions if any will come here

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ragapp",
    user="ajaykrishna22",
    password=""
)

cursor = conn.cursor()

query = """
    INSERT INTO documents (workspace_id, body, embedding)
    VALUES (%s, %s, %s::vector);
"""
test_embedding = [1.0] + [0.0] * 383
values = (2, "ajay Krishna", test_embedding)
cursor.execute(query, values)

cursor.execute("SELECT id FROM documents where workspace_id=2;")

records = cursor.fetchall()

print(type(records))
print(type(records[0]))
print(records)