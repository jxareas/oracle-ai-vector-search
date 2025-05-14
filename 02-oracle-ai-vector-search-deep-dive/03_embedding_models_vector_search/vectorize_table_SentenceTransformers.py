import os
import sys
import array
import time
import oracledb
from sentence_transformers import SentenceTransformer

un = os.getenv("PYTHON_USERNAME")
pw = os.getenv("PYTHON_PASSWORD")
cs = os.getenv("PYTHON_CONNECTSTRING")

# Select one of the available embedding models
embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
#embedding_model = "sentence-transformers/all-MiniLM-L12-v2"
#embedding_model = "sentence-transformers/paraphrase-MiniLM-L3-v2"
#embedding_model = "sentence-transformers/all-mpnet-base-v2"
#embedding_model = "sentence-transformers/all-distilroberta-v1"
#embedding_model = "BAAI/bge-small-en-v1.5"
#embedding_model = "BAAI/bge-base-en-v1.5"
#embedding_model = "sentence-transformers/average_word_embeddings_glove.6B.300d"
#embedding_model = "sentence-transformers/average_word_embeddings_komninos"
#embedding_model = "nomic-ai/nomic-embed-text-v1"
#embedding_model = "BAAI/bge-m3"
#embedding_model = "intfloat/multilingual-e5-large"
#embedding_model = "intfloat/multilingual-e5-base"
#embedding_model = "intfloat/multilingual-e5-small"
#embedding_model = "paraphrase/multilingual-mpnet-base-v2"
#embedding_model = "distiluse-base-multilingual-cased-v2"
#embedding_model = "stsb-xlm-r-multilingual"

# Load the selected model
model = SentenceTransformer(embedding_model)

query_sql = """select id, info
    from my_data
    order by 1"""

update_sql = """update my_data set v = :1
    where id = :2"""

# Connect to Oracle Database 23.6
with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    db_version = tuple(int(s) for s in connection.version.split("."))[:2]
    if db_version < (23, 4):
        sys.exit("This example requires Oracle Database 23.4 or later")
    print("Connected to Oracle Database\n")

    with connection.cursor() as cursor:
        print("Vectorizing the following data:\n")

        # Loop over the rows and vectorize the VARCHAR2 data
        binds = []
        tic = time.perf_counter()

        for id_val, info in cursor.execute(query_sql):
            # Convert to input string format for Sentence Transformers
            data = f"{info}"

            # Create the embedding and extract the vector
            embedding = list(model.encode(data))

            # Convert to array format
            vec2 = array.array("f", embedding)

            # Record the array and key
            binds.append([vec2, id_val])

            print(info)

        toc = time.perf_counter()

        # Do an update to add or replace the vector values
        cursor.executemany(update_sql, binds)
        connection.commit()

print(f"Vectors took {toc - tic:0.3f} seconds")
print(f"\nAdded {len(binds)} vectors to the table using embedding model: " + embedding_model + "\n")