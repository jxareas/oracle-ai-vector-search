# Finding Closest Vectors - Questions

1. **What is a potential drawback of Exact Similarity Search?**
    - [ ] Use of vector indexes
    - [x] Significant search times
    - [ ] Inaccurate results
    - [ ] Limited accuracy

   **Explanation:** While Exact Similarity Search offers perfect search quality and the most accurate results, it can
   potentially result in significant search times.

2. **Multi-Vector Similarity Search is typically used for:**
    - [ ] Single-vector comparisons
    - [ ] Exact vector matching
    - [x] Multi-document search
    - [ ] Image recognition

   **Explanation:** Multi-Vector Similarity Search is primarily employed for searches involving multiple documents. In
   this approach, documents are divided into chunks, and each chunk is embedded into individual vectors for comparison
   and retrieval.

3. **What concept can be applied to vectorized data that is not uniformly distributed?**
    - [ ] Dimensionality reduction
    - [x] Clustering
    - [ ] Indexing
    - [ ] Normalization

   **Explanation:** Vectorized data can form clusters, representing groups of similar data. These clusters arise because
   the data is not evenly spread out (uniformly distributed).

4. **Based on the sources, which of these is a valid way to construct a vector with the values (10, 20) using
   the `VECTOR()` constructor?**
    - [ ] `VECTOR ('[10, 20]')`
    - [ ] `VECTOR ('[10, 20]')`
    - [ ] `VECTOR ['10, 20']`
    - [x] `VECTOR (10, 20)`

   **Explanation:** VECTOR ( '[value1, value2]' ) is used to create vectors. Square brackets and commas are used within
   the string to delimit the vector values. The other options do not follow the syntax required to create vectors.

5. **Which of the following is NOT a characteristic of Approximate Similarity Search?**
    - [x] Always provides exact matches
    - [ ] Uses vector indexes
    - [ ] Uses target accuracy
    - [ ] Can be more efficient

   **Explanation:** Approximate Similarity Search leverages vector indexes to enhance efficiency but may not always
   produce exact matches. It aims for a target accuracy level rather than perfect precision.

 
