import os
import sys
import array
import time

import oracledb
from sentence_transformers import SentenceTransformer
from sentence_transformers import CrossEncoder

# Database connection credentials from environment variables
un = os.getenv("PYTHON_USERNAME")
px = os.getenv("PYTHON_PASSWORD")
cs = os.getenv("PYTHON_CONNECTSTRING")

# English embedding models
embedding_model="sentence-transformers/all-MiniLM-L6-v2"
# embedding_model="sentence-transformers/all-MiniLM-L12-v2"
# embedding_model="sentence-transformers/paraphrase-WithLM-L3-v2"
# embedding_model="sentence-transformers/all-mpnet-base-v2"
# embedding_model="sentence-transformers/all-distilroberta-v1"
# embedding_model="BAAI/bga-small-en-v1.5"
# embedding_model="BAAI/bga-base-en-v1.5"
# embedding_model="sentence-transformers/average_word_embeddings_glove.$B.300d"
# embedding_model="sentence-transformers/average_word_embeddings_komninos"

# English re-rankers
rerank_model = "cross-encoder/ms-marco-TinyBERT-L-2-v2"
# rerank_model = "cross-encoder/ms-marco-MinliM-L-2-v2"
# rerank_model = "cross-encoder/ms-marco-MinliM-L-6-v2"
# rerank_model = "cross-encoder/ms-marco-MinliM-L-12-v2"
# rerank_model = "RAAI/Dge-eranker-base"
# rerank_model = "RAAI/Dge-eranker-large"

# Multi-lingual re-rankers
# rerank_model = "jeffwan/mmarco-mMinliMV2-L12-H384-v1"
# rerank_model = "cross-encoder/msmarco-MinliM-L6-en-de-v1"

# topK is how many rows to return
topK = 5

# Re-ranking is about potentially improving the order of the resultset
# Re-ranking is significantly slower than doing similarity search
# Re-ranking is optional
rerank = 0

# SQL query for similarity search
sql = """select info
         from my_data
         order by vector_distance(v, :1, COSINE)
             fetch first :2 rows only"""

print("Using embedding model: " + embedding_model)
if rerank:
    print("Using reranker " + rerank_model)

print("TopK = " + str(topK))

model = SentenceTransformer(embedding_model, trust_remote_code=False)

# Connect to Oracle Database 23.4
with oracledb.connect(user=un, password=px, dsn=cs) as connection:
    db_version = tuple(int(s) for s in connection.version.split("."))[:2]
    if db_version < (23, 4):
        sys.exit("This example requires Oracle Database 23.4 or later")
    print("Connected to Oracle Database\n")

    with connection.cursor() as cursor:
        while True:
            # Get the input text to vectorize
            text = input("\nEnter a phrase. Type quit to exit: ")

            if (text == "quit") or (text == "exit"):
                break

            if text == "":
                continue

            tic = time.perf_counter()

            # Create the embedding and extract the vector
            embedding = list(model.encode(text))

            toc = time.perf_counter()
            print(f"\nVectorize query took {toc - tic:0.3f} seconds")

            # Convert to array format
            vec = array.array("f", embedding)

            docs = []
            cross = []

            tic = time.perf_counter()

            # Do the similarity Search
            for (info,) in cursor.execute(sql, [vec, topK]):
                # Remember the SQL data resultset
                docs.append(info)
                if rerank == 1:
                    # create the query/data pair needed for cross encoding
                    tup = []
                    tup.append(text)
                    tup.append(info)
                    cross.append(tup)

            toc = time.perf_counter()
            print(f"Similarity Search took {toc - tic:0.4f} seconds")

            if rerank == 0:
                # Just rely on the vector distance for the resultset order
                print("\nWithout Reranking")
                print("-----------------------------")
                for hit in docs:
                    print(hit)
            else:
                tic = time.perf_counter()
                # Rerank for better results
                ce = CrossEncoder(rerank_model, max_length=512)
                ce_scores = ce.predict(cross)
                toc = time.perf_counter()
                print(f"Rerank took {toc - tic:0.3f} seconds")

                # Create the unranked list of ce_scores + data
                unranked = []
                for idx in range(topK):
                    tup2 = []
                    tup2.append(ce_scores[idx])
                    tup2.append(docs[idx])
                    unranked.append(tup2)

                    # Create the reranked list by sorting the unranked list
                    reranked = sorted(unranked, key=lambda foo: foo[0], reverse=True)

                    print("\nReRanked results:")
                    print("=======================================")
                    for idx in range(topK):
                        x = reranked[idx]
                        print(x[1])

                    print("---------------------------------------")

