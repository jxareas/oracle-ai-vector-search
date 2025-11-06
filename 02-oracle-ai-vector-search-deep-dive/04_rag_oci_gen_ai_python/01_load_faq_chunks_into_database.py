import json
import array
import oracledb
import os
from sentence_transformers import SentenceTransformer
from load_faqs_function import load_faqs

# Database credentials
un = os.getenv("PYTHON_USERNAME")
pw = os.getenv("PYTHON_PASSWORD")
cs = os.getenv("PYTHON_CONNECTSTRING")

# Establish connection
connection = oracledb.connect(user=un, password=pw, dsn=cs)

script_dir = os.path.dirname(os.path.abspath(__file__))
# Data Loading
data_faqs = load_faqs(os.path.join(script_dir))

docs = [{'text': filename + ' | ' + section,
         'path': filename}
        for filename, sections in data_faqs.items()
        for section in sections]

# Table creation
table_name = 'faqs'
create_table_sql = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    payload CLOB CHECK (payload IS JSON),
    vector VECTOR
)
"""

try:
    with connection.cursor() as cursor:
        cursor.execute(create_table_sql)
except oracledb.DatabaseError as e:
    raise
finally:
    connection.autocommit = True

# Encoder initialization
encoder = SentenceTransformer('all-MiniLM-L6-v2')

# 1. Prepare data structure
data = [
    {"id": idx, "vector_source": row['text'], "payload": row, "vector": None}
    for idx, row in enumerate(docs)
]

# 2. Batch encode texts
texts = [row['vector_source'] for row in data]
embeddings = encoder.encode(texts, batch_size=32, show_progress_bar=True)

# 3. Store embeddings
for row, embedding in zip(data, embeddings):
    row['vector'] = array.array("f", embedding)  # 'f' for float array

# 4. Database operations
with connection.cursor() as cursor:
    # Truncate table
    cursor.execute(f"TRUNCATE TABLE {table_name}")

    # Prepare insert data
    prepared_data = [
        (json.dumps(row['payload']), row['vector'])
        for row in data
    ]

    # Bulk insert
    cursor.executemany(
        f"INSERT INTO {table_name} (payload, vector) VALUES (:1, :2)",
        prepared_data
    )

# 5. Verification query
with connection.cursor() as cursor:
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows[:5]:  # Print first 5 rows
        print(row)