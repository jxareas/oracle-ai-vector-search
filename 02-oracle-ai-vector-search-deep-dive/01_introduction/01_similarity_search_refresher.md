# Similarity Search Refresher

## Similarity Search

Vector Distance functions can be used to compute numerical similarity. Vector embeddings which are **numerically
similar** are also **semantically similar**.

There are several types of similarity searches, such as:

- **Exact similarity search**: Visits vectors across all clusters.
    ```oracle
    SELECT docID FROM vector_tab
    ORDER BY VECTOR_DISTANCE(embedding, :query_vector, EUCLIDEAN)
    FETCH FIRST 10 ROWS ONLY;
   ```
- **Approximate similarity search**: Uses vector indexes. It can limit the search to specific clusters.
    ```oracle
    SELECT chunk_id, chunk_data FROM doc_chunks
    ORDER BY VECTOR_DISTANCE(chunk_embedding, :query_vector, COSINE)
    FETCH APPROX FIRST 4 ROWS ONLY
    WITH TARGET ACCURACY 80;
   ```
- **Multi-vector similarity search**: Useful when you have multiple related vectors, allows us to create hierarchical
  searches, such as:
    - Find the best 2 books
    - Within those books, find the best 3 paragraphs
    - Within those paragraphs, find the best 3 sentences
  ```oracle
  SELECT bookId, paragraphId, sentence
  FROM books
  ORDER BY vector_distance(sentence_embedding, :query_vector)
  FETCH FIRST 2 PARTITIONS BY bookId,
  3 PARTITIONS BY paragraphId,
  4 ROWS ONLY
   ```

| Type                           | Description                                                                                                                                                             | Benefits                                                                                                                | Drawbacks                                                                                              |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Exact Similarity Search        | Calculates the distance between a query vector and every other vector in the dataset to determine the relative order of vectors.                                        | Produces the most accurate result with perfect search quality.                                                          | Can have significant search times, especially for large datasets.                                      |
| Approximate Similarity Search  | Utilizes vector indexes to speed up searches by trading off some accuracy for performance.                                                                              | Faster search speeds, especially for large vector spaces.                                                               | Less accurate than exact similarity search. May return fewer than k rows in a top-k similarity search. |
| Multi-Vector Similarity Search | Retrieves top-k vector matches using grouping criteria known as partitions. This allows scoring of documents based on the similarity of their chunks to a query vector. | Facilitates complex queries involving multiple levels of grouping. Can be used for tasks such as multi-document search. |                                                                                                        |



