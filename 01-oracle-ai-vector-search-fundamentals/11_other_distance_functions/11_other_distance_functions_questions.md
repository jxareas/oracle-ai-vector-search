# Other Distance Functions - Questions

1. **If the `VECTOR_DISTANCE()` function is used with the `HAMMING` metric, what characteristic of the vectors is being
   compared?**
    - [ ] The angle between the vectors.
    - [x] The number of components that have different values.
    - [ ] The product of the corresponding components.
    - [ ] The sum of the absolute differences between corresponding components.
2. **What is the purpose of using alternative distance functions like cosine similarity, dot product, or Manhattan
   distance when comparing vectors?**
    - [x] To measure different aspects of similarity or dissimilarity between vectors, beyond Euclidean distance.
    - [ ] To normalize the vectors before calculating distances, ensuring fair comparisons.
    - [ ] To improve the speed of vector comparisons, especially for high-dimensional vectors.
    - [ ] To handle cases where the vectors have missing or incomplete data.
3. **Which shorthand notation in Oracle Database 23ai represents cosine similarity between two vectors, v1 and v2?**
    - [ ] `v1 <+> v2`
    - [ ] `v1 <-> v2`
    - [ ] `v1 <#> v2`
    - [x] `v1 <=> v2`
4. **What is the main advantage of using shorthand syntax like `<->` or `<#>` for vector distance calculations?**
    - [ ] It enables the use of custom-defined distance functions.
    - [x] It improves the readability and conciseness of SQL queries.
    - [ ] It allows for more complex mathematical operations.
    - [ ] It reduces computational overhead.
5. **Which vector distance function is equivalent to the shorthand syntax `v1 <-> v2` in Oracle Database 23ai?**
    - [ ] `INNER_PRODUCT(v1, v2)`
    - [ ] `COSINE_DISTANCE(v1, v2)`
    - [x] `L2_DISTANCE(v1, v2)`
    - [ ] `L1_DISTANCE(v1, v2)`