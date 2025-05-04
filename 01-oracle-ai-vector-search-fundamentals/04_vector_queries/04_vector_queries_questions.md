# Oracle AI Vector Search Queries - Test Questions

1. **What type of data can be used for creating Vector Embeddings?**
    - [ ] Image data
    - [ ] Audio data
    - [ ] Text data
    - [x] <span style="color:red">All of the above</span>

2. **Considering the limitations of comparison operations between vectors, which approach would be suitable for finding
   vectors similar to a query vector q in a table named items with a vector column named embedding?**
    - [ ] SELECT * FROM items WHERE embedding = q
    - [ ] SELECT * FROM items WHERE embedding < q
    - [ ] Convert the vectors to string representations and compare them using string matching functions.
    - [x] <span style="color:red">Use specialized functions or libraries that calculate vector distances or
      similarities.</span>

3. **Which of the following SQL statements correctly inserts a vector into a table named product_embeddings with a
   column named embedding of the VECTOR data type?**
    - [ ] INSERT INTO product_embeddings VALUES ( '[0.1, 0.2, 0.3]')
    - [x] <span style="color:red">INSERT INTO product_embeddings VALUES ( VECTOR (0.1, 0.2, 0.3))</span>
    - [ ] INSERT INTO product_embeddings VALUES ((0.1, 0.2, 0.3))
    - [ ] INSERT INTO product_embeddings VALUES ( '[0.1, 0.2, 0.3])

4. **What does the error message "ORA-22848: cannot use VECTOR type as comparison key" indicate?**
    - [ ] The dimensionality of the vectors being compared is incompatible.
    - [ ] The VECTOR data type is not supported for indexing purposes.
    - [x] <span style="color:red">An attempt was made to compare two vectors using operators like = or <.</span>
    - [ ] The query is trying to insert a vector with incorrect formatting.

5. **Which of the following mathematical operations can be directly performed between two vectors (v1 and v2) using
   built-in functions or operators in Oracle Database 23ai?**
    - [ ] Addition (v1 + v2)
    - [ ] Subtraction (v1 - v2)
    - [ ] Multiplication (v1 - v2)
    - [x] <span style="color:red">None of these</span>
