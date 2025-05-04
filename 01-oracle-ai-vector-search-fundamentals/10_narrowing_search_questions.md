# Narrowing Search Results - Questions

1. **What is the primary purpose of using the `VECTOR_DISTANCE()` function in a SQL query?**
    - [x] To calculate the distance between vectors for similarity comparison.
    - [ ] To group data points based on their color attributes.
    - [ ] To determine the geometric shape of the data points.
    - [ ] To sort the results in ascending order of their IDs.

   **Explanation:** The `VECTOR_DISTANCE()`  function is used to compute the distance between vectors, which serves as a
   measure of similarity. This distance calculation is crucial for finding the closest vectors to the target vector.

2. **Assuming we have a table called `VT2` that contains vectors for mapping various shapes, colors, and sizes, what is
   the primary purpose of the following UPDATE statements?**

   ```oraclesqlplus
   UPDATE vt2  
   SET shape = 'Triangle'  
   WHERE id IN (2, 4, 7, 22, 31, 41, 44, 55);  

   UPDATE vt2  
   SET size = 'Medium'  
   WHERE id IN (5, 22, 25, 32, 34, 42, 43, 53, 54, 55);  
   ```  

    - [ ] To add new rows of data to the `VT2` table with different sizes and shapes.
    - [ ] To modify the vector values stored in the `VT2` table.
    - [x] To assign attributes like size and shape to existing vectors based on their IDs.
    - [ ] To delete rows from the `VT2` table that do not meet specific criteria.

   **Explanation:** The `UPDATE` statements are used to populate the `SIZE` and `SHAPE` columns of the `VT2` table.
   These columns are added to the table to store attributes associated with each vector. The `UPDATE` statements use
   `WHERE` clauses to selectively modify rows based on their `ID`, linking specific attributes to corresponding vectors.

3. **What data types can be used for the components of a `VECTOR` column in Oracle Database 23ai?**
    - [ ] `NUMBER` only
    - [ ] `FLOAT` only
    - [ ] `VARCHAR2` only
    - [x] Both `NUMBER` and `FLOAT`

   **Explanation:**  `VECTOR()` constructor can be used with both `NUMBER` and `FLOAT` data types for the vector
   elements. E.g., `VECTOR('', 2, FLOAT32)` uses a `FLOAT` data type. Implicitly, when no data type is specified,
   the examples suggest that `NUMBER` is the assumed data type.

4. **What is Exact Similarity Search also called?**
    - [ ] Efficient search
    - [ ] Vector search
    - [ ] Approximate search
    - [x] Flat search

   **Explanation:** Exact Similarity Search is also referred to as Flat Search.

5. **In the following SQL query, which distance function should replace the `FUNCTION` keyword to find the closest
   vectors?**

   ```oraclesqlplus
   SELECT id, vsize, shape, color,  
   to_number(FUNCTION(vector([16, 3]), v, EUCLIDEAN)) distance  
   FROM vt2  
   WHERE id > 30 AND id < 40  
   ORDER BY VECTOR_DISTANCE(vector([16, 3]), v, EUCLIDEAN)  
   FETCH FIRST 3 ROWS ONLY;  
   ```  

    - [ ] `COSINE_DISTANCE`
    - [x] `VECTOR_DISTANCE`
    - [ ] `INNER_PRODUCT`
    - [ ] `L1_DISTANCE`

   **Explanation:** `VECTOR_DISTANCE` calculates the distance between two vectors using a specific metric
   (like Euclidean distance). It is the most appropriate choice for finding the closest vectors. `COSINE_DISTANCE`
   measures the cosine of the angle between two vectors, which is useful for understanding the orientation of the
   vectors rather than their absolute distances. It is not suitable for finding the "closest" vectors in terms of
   Euclidean distance. `INNER_PRODUCT` computes the dot product of two vectors. While it can provide some insights into
   the similarity of the vectors, it does not directly measure distance. `L1_DISTANCE`, also known as Manhattan
   distance, sums the absolute differences of their coordinates. While it's another way to measure distance, the query
   specifies using Euclidean distance, making this option less suitable in this context.

