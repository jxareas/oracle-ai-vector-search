# Oracle AI Vector Search Workflow - Test Questions

1. **What types of searches can be combined when querying data in Oracle Database 23ai that includes
   vector embeddings?**
    - [ ] Image recognition searches and natural language processing.
    - [x] <span style="color:red">Similarity searches and relational searches.</span>
    - [ ] Keyword searches and sentiment analysis.
    - [ ] Geospatial searches and time-series analysis.

   **Explanation:** Oracle Database 23ai allows for the combination of "Similarity searches" and "Relational searches."
   This powerful capability enables users to perform complex queries that leverage both the semantic relationships
   captured in vector embeddings (similarity searches) and the structured information stored in relational tables (
   relational searches). This combined approach offers greater flexibility and precision in retrieving relevant data.

2. **What is the main advantage of creating Vector Indexes in Oracle Database 23ai?**
    - [ ] They convert relational data into vector representations.
    - [ ] They compress the vector data, reducing storage space.
    - [x] <span style="color:red">They enable efficient searching for similar vectors in large vector spaces.</span>
    - [ ] They allow for direct comparison of vectors using operators like `=` or `<`.

   **Explanation**: Vector Indexes can optimize vector search operations. These indexes are specifically designed to
   handle the challenges of searching for similar vectors within potentially vast vector spaces. They employ various
   techniques to speed up the search process, making it feasible to find relevant vectors efficiently even when
   dealing with massive amounts of data.

3. **What is the first step in the Oracle AI Vector Search Workflow?**
    - [ ] Query Data with Similarity Searches
    - [ ] Store Vector Embeddings
    - [x] <span style="color:red">Generate Vector Embeddings</span>
    - [ ] Vector Indexes

   **Explanation**: The initial step in the Oracle AI Vector Search workflow is to "Generate Vector Embeddings." Vector
   embeddings are
   mathematical representations of data points (like text, images, or other unstructured content) in a multidimensional
   vector space. Generating these embeddings is the foundation for enabling similarity searches within the Oracle
   Database environment.

4. **Where can vector embeddings be generated in Oracle Database 23ai?**
    - [ ] Only within the database
    - [ ] Nowhere, vector embeddings are not generated
    - [ ] Only outside the database
    - [x] <span style="color:red">Both outside and within the database</span>

   **Explanation**: Vector embeddings can be generated "Outside the DB" and "Within the DB." Oracle Database 23ai offers
   flexibility in terms of where these embeddings can be created. Users can choose to generate embeddings using external
   tools or services and then import them into the database. Alternatively, they can leverage the capabilities of Oracle
   Database 23ai itself to generate embeddings directly within the database environment.

5. **How are vector embeddings stored in Oracle Database 23ai?**
    - [ ] They are appended as metadata to existing data files.
    - [ ] They are not stored; they are only used for querying.
    - [ ] They are stored in a separate, specialized vector database.
    - [x] <span style="color:red">By creating columns with the `VECTOR` data type in relational tables.</span>

   **Explanation**:  Embeddings are stored by creating columns with the data type `VECTOR` within the relational tables
   of the database. This approach integrates vector data seamlessly into the existing relational database structure,
   allowing for efficient management and querying alongside other business data.
