# RAG with Oracle AI Generative AI Service using Python

## OCI Generative AI Service

**OCI Generative AI Service** is a fully managed cloud offering within Oracle Cloud Infrastructure (OCI) designed
to empower enterprises with scalable, secure and customizable Generative AI solutions.z

It integrates state-of-the-art large language models (LLMs) and tools to build, fine-tune and deploy AI-driven
applications across industries.

It allows us to:

- Transform user questions into augmented retrieval content.
- Leverage Oracle AI Vector Search to retrieve contextually relevant information.
- Creates prompts as inputs for retrieving using Large Language Models (LLMs).

## Oracle AI Vector Search & OCI Generative AI Service (using python)

Here are the typical steps for a full RAG pipeline using Oracle AI Vector Search with python and OCI Generative
AI Service:

1. Load the document.
   Load the text sources from a file.
2. Transform the document to text.
   Transforming the previously loaded document to a text (python `string`).
3. Split the text into chunks.
   We will split the previously created `string` into several `string`s (text chunks).
4. Set up Oracle AI Vector Search and insert the embedding vectors.
   Loading the text chunks into the database:
    - Create a connection and connect to the database instance.
    - Create the table.
    - Vectorize the text chunks.
    - Encode the text content.
    - Insert the text chunks and vectors into the database.
5. Build the prompt to query the document.
   Now we vectorize the question:
    - Define the script ordering the results by the calculated score and define the question. Finally, write the
      retrieval code.
    - Create the LLM prompt and call the Generative AI LLM: Initialize the OCI client, build the prompt and make the
      call.
6. Invoke the chain.
   Executed the aforementioned steps one by one, in order to perform a full RAG pipeline.
