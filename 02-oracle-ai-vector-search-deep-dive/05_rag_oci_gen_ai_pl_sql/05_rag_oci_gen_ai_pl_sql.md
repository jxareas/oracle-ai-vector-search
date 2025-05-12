# RAG with Oracle AI Generative AI Service using PL/SQL

Here are the typical steps for a full RAG pipeline using Oracle AI Vector Search with PL/SQL and OCI Generative
AI Service:

1. Text Extraction and Preparation.
    - Load the document.
    - Transform the document to text.
    - Split the text into chunks.
2. Embedding models and vectorization.
    - Load multiple ONNX models into the database.
    - Create vector embeddings using PL/SQL packages.
    - Compare vector embeddings using different embedding models.
3. Similarity search and response generation.
    - Select the text chunks that has relevant information for the user question based on vector search.
4. Build the prompt.
    - **LLM Prompt Engineering**: enables us to craft input queries or instructions to create more accurate and
      desirable
      outputs.
    - [Optional] Create a simple user-friendly interface using frameworks like Streamlit.
5. Invoke the chain.
   Executed all the steps mentioned above in order to perform the full RAG pipeline.
