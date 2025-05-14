import array
import json
import oracledb
from sentence_transformers import SentenceTransformer

un = "vector"
pw = "vector"
cs = "localhost/alpha"

# Establish connection and encoder
connection = oracledb.connect(user=un, password=pw, dsn=cs)
encoder = SentenceTransformer('all-MiniLM-L6-v2')

topK = 3
sql = f"""select payload, vector_distance(vector, :vector, COSINE) as score from {table_name}
order by score
fetch approx first {topK} rows only"""

question = "What is always free?"

with connection.cursor() as cursor:
    embedding = list(encoder.encode(question))
    vector = array.array("f", embedding)

    results = []

    for (info, score) in cursor.execute(sql, [vector]):
        text_content = info.read()
        results.append((score, json.loads(text_content)))
