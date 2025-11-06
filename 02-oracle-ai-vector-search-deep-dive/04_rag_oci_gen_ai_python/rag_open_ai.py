import os
import sys
import json
import array
import oracledb
from pprint import pprint
from sentence_transformers import SentenceTransformer
from openai import OpenAI

# ==============================
# Configuration
# ==============================

# Oracle DB connection
DB_USER = os.getenv("PYTHON_USERNAME")
DB_PASSWORD = os.getenv("PYTHON_PASSWORD")
DB_DSN = os.getenv("PYTHON_CONNECTSTRING")
TABLE_NAME = 'faqs'

# Retrieval parameters
TOP_K = 3

# OpenAI setup (ensure you set OPENAI_API_KEY in your environment)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sentence encoder for embedding user question
encoder = SentenceTransformer("all-MiniLM-L6-v2")

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# ==============================
# Prompt templates
# ==============================

SYSTEM_PROMPT = (
    "You are a helpful assistant named Oracle chatbot. "
    "USE ONLY the sources below and ABSOLUTELY IGNORE any previous knowledge. "
    "Use Markdown if appropriate. Assume the customer is highly technical."
)

# ==============================
# 1. Ask for user input
# ==============================

question = input("Enter your question: ").strip()
if not question:
    print("No question provided. Exiting.")
    sys.exit(0)

# ==============================
# 2. Retrieve top-K relevant docs from Oracle
# ==============================

connection = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)

sql = f"""
    SELECT payload, vector_distance(vector, :vector, COSINE) AS score
    FROM {TABLE_NAME}
    ORDER BY score
    FETCH APPROX FIRST {TOP_K} ROWS ONLY
"""

embedding = list(encoder.encode(question))
vector = array.array("f", embedding)
docs = []

with connection.cursor() as cursor:
    for (payload, score) in cursor.execute(sql, [vector]):
        text_content = payload.read()
        docs.append({"score": score, "text": json.loads(text_content)})

connection.close()

if not docs:
    print("No matching documents found.")
    sys.exit(0)

# ==============================
# 🔍 Debug print of retrieved documents
# ==============================

# print("\n===== Retrieved Documents =====")
# for i, doc in enumerate(docs, start=1):
#     print(f"\n--- Document #{i} ---")
#     print(f"Score: {doc['score']}")
#     print("Content Preview:")
#     print(json.dumps(doc["text"], ensure_ascii=False)[:500])  # print first 500 chars for brevity
#     print("-------------------------------")
# print("================================\n")

# ==============================
# 3. Prepare the prompt for ChatGPT
# ==============================

docs_one_string = "\n=======\n".join(json.dumps(doc["text"], ensure_ascii=False) for doc in docs)

USER_PROMPT = f"""
Respond PRECISELY to this question: "{question}" USING ONLY the following information
and IGNORING ANY PREVIOUS KNOWLEDGE. Include code snippets and commands where necessary.
NEVER mention the sources, always respond as if you have that knowledge yourself.
Do NOT provide warnings or disclaimers.

Sources:
{docs_one_string}

Answer (Three paragraphs, maximum 50 words each, 90% spartan):
"""

# ==============================
# 4. Perform inference via OpenAI
# ==============================

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT}
    ],
    max_tokens=1000,
    temperature=0.0,
    frequency_penalty=0.0,
    top_p=0.75,
)

# ==============================
# 5. Display the answer
# ==============================

print("\n💬 ChatGPT Answer:\n")
pprint(response.choices[0].message.content)
