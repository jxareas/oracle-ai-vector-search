# Oracle Vector DDL - Test Questions

# Oracle Vector Search and Memory Management - Test Questions

1. **Which SQL statement correctly adds a VECTOR column named v with 3 dimensions and FLOAT32 format to an existing
   table named my_table?**
    - [x] `ALTER TABLE my_table ADD v VECTOR(3, FLOAT32)`
    - [ ] `ALTER TABLE my_table ADD (v VECTOR(3, FLOAT32))`
    - [ ] `ALTER TABLE my_table MODIFY (v VECTOR(3, FLOAT32))`
    - [ ] `UPDATE my_table SET v = VECTOR(3, FLOAT32)`

   **Explanation:** The correct syntax for adding a new VECTOR column requires using the `ADD` clause with corresponding
   vector column definition. The `MODIFY` clause is for changing existing columns, and `UPDATE` is for data
   manipulation, not schema changes.

2. **Can you create a table with multiple VECTOR columns?**
    - [x] Yes, a table can have multiple VECTOR columns.
    - [ ] Yes, but only if all VECTOR columns have the same dimensions.
    - [ ] No, a table can only have one VECTOR column.
    - [ ] No, VECTOR columns can only be added to existing tables.

   **Explanation:** Oracle Database allows multiple VECTOR columns in a single table, and these columns can have
   different dimensions from each other. There is no restriction on the number of VECTOR columns per table.

3. **Which of the following DDL operations is NOT permitted on a table containing a VECTOR column in Oracle Database
   23ai?**
    - [x] Modifying the data type of an existing `VECTOR` column to a non-VECTOR type (e.g., VARCHAR2).
    - [ ] Dropping an existing VECTOR column from the table.
    - [ ] Adding a new VECTOR column to the table.
    - [ ] Creating a new table using `CREATE TABLE AS SELECT` that includes the `VECTOR` column from the original table.

   **Explanation:** While you can drop or add VECTOR columns, Oracle Database does not allow changing a VECTOR column to
   a non-VECTOR data type. `CTAS` operations with `VECTOR` columns are fully supported.

4. **What is the maximum number of dimensions a `VECTOR` data type can have in Oracle Database 23ai?**
    - [ ] 4,096
    - [ ] 1,024
    - [x] 65,536
    - [ ] 1,536

   **Explanation:** Oracle Database 23ai supports vectors with up to 65,536 dimensions, providing flexibility for
   high-dimensional vector embeddings used in modern AI applications.

5. **Which of the following statements is NOT true regarding operations on VECTOR columns?**
    - [ ] You can update a VECTOR column based on the value of another column in the same table.
    - [x] You can perform direct comparisons between two VECTOR columns using operators like '='.
    - [ ] You can use `CTAS` (Create Table As Select) to create a new table with a VECTOR column based on an existing
      table.
    - [ ] You can drop a `VECTOR` column from a table using ALTER TABLE... DROP COLUMN.

   **Explanation:** Direct comparison of `VECTOR` columns using standard operators like '=' is not supported. Vector
   similarity must be calculated using specialized functions like VECTOR_DISTANCE() or through vector search operations.