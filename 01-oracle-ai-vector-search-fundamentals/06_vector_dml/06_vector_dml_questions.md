# Oracle Vector DML - Test Questions

1. **Which of the following SQL statements will successfully insert a vector into a table named vectors with a single
   VECTOR column named v?**
    - [ ] `INSERT INTO vectors VALUES ([1.1, 2.2, 3.3])`
    - [ ] `INSERT INTO vectors (v) VALUES (1.1, 2.2, 3.3)`
    - [ ] `INSERT INTO vectors VALUES ('[1.1, 2.2, 3.3]')`
    - [x] `INSERT INTO vectors (v) VALUES ('[1.1, 2.2, 3.3]')`

   **Explanation:** The correct syntax for inserting a vector requires specifying the column name (v) and enclosing the
   vector values in square brackets as a string. The other options either use incorrect syntax or fail to properly
   format the vector data.

2. **What happens when you attempt to insert a vector with an incorrect number of elements into a VECTOR column with a
   defined number of dimensions?**
    - [ ] The database truncates the vector to fit the defined dimensions.
    - [ ] The database ignores the defined dimensions and inserts the vector as is.
    - [x] The insert operation fails, and an error message is thrown.
    - [ ] The database pads the vector with zeros to match the defined dimensions.

   **Explanation:** Oracle Database enforces the defined dimensionality of VECTOR columns. Any attempt to insert a
   vector with an incorrect number of elements will result in a failed operation and an error message, ensuring data
   integrity.

3. **When defining a VECTOR column, what does specifying the number of dimensions achieve?**
    - [ ] It determines the precision of the numeric values stored in the vector.
    - [ ] It specifies the type of data that can be stored in the vector (e.g., text, image).
    - [x] It enforces the number of elements allowed in the vector.
    - [ ] It improves the performance of similarity searches.

   **Explanation:** Specifying the number of dimensions for a VECTOR column defines the fixed number of elements that
   each vector in that column must contain. This constraint is enforced during data insertion and updates.

4. **How can vector data be manipulated within an Oracle Database using Data Manipulation Language (DML)?**
    - [ ] Insertion and updates
    - [ ] Insertion only
    - [ ] Insertion, updates, and deletion
    - [x] Insertion, updates, deletion, and loading

   **Explanation:** Vector data in Oracle Database supports full DML operations, including insertion, updates, deletion,
   and loading. This comprehensive support allows for flexible management of vector data within the database.

5. **Examine the following SQL statement:**
   ```sql
   CREATE TABLE my_vectors (id NUMBER, embedding VECTOR);
   ```
   What is the default number format for the "embedding" column?
    - [ ] INT8
    - [ ] FLOAT64
    - [ ] BINARY_DOUBLE
    - [x] FLOAT32

   **Explanation:** When no format is explicitly specified for a `VECTOR` column, Oracle Database defaults to FLOAT32 as the
   number format for the vector elements.