# Creating and Finding Nearest Vectors - Questions

1. **You need to find the Euclidean distance between the vectors (0, 0) and (3, 4). Which SQL statement will produce the
   correct result?**
    - [ ] `SELECT EUCLIDEAN_DISTANCE (VECTOR('[0,0]'), VECTOR('[3,4]'))`
    - [x] `SELECT VECTOR_DISTANCE (VECTOR('[0,0]'), VECTOR('[3,4]'), EUCLIDEAN)`
    - [ ] `SELECT VECTOR_DISTANCE (('[0, 0]'), ('[3, 4]'))`
    - [ ] `SELECT VECTOR_DISTANCE (", (3, 4))`

   **Explanation:** `VECTOR_DISTANCE()` takes three arguments: the first vector (created using `VECTOR()` constructor),
   the second vector (also created using `VECTOR()` constructor), and the distance metric to use (which is `EUCLIDEAN`
   in this case). Vector coordinates should be properly formatted when passed to the `VECTOR()` constructor. There is
   `EUCLIDEAN_DISTANCE` function, but `L2_DISTANCE` (which is the same conceptually).

2. **Which of the following SQL statements correctly creates a two-dimensional vector with the coordinates (4, -3) using
   the VECTOR() constructor?**
    - [x] `SELECT VECTOR('[4, -3]')`
    - [ ] `SELECT VECTOR(4 -3)`
    - [ ] `SELECT VECTOR(4, -3)`
    - [ ] `SELECT VECTOR('(4, -3)')`

   **Explanation:** Vector coordinates are enclosed within square brackets and passed as a single string argument to the
   `VECTOR()` constructor. The correct syntax for creating a vector with coordinates (4, -3) is `SELECT VECTOR(4, -3)`.

3. **You have a table named images with columns for `image_id` and a VECTOR column named `feature_vector`. You want to
   create a new table named `image_subset` that contains only the `image_id` and `feature_vector` columns for images
   with an image_id greater than 1000. Which SQL statement would achieve this?**
    - [ ] `INSERT INTO image_subset SELECT image_id, feature_vector FROM images WHERE image_id > 1000`
    - [ ] `ALTER TABLE images CREATE TABLE image_subset AS SELECT image_id, feature_vector WHERE image_id > 1000`
    - [x] `CREATE TABLE image_subset AS SELECT image_id, feature_vector FROM images WHERE image_id > 1000`
    - [ ] `COPY TABLE image_subset FROM images WHERE image_id > 1000`

   **Explanation:** A `CREATE TABLE AS SELECT` (CTAS) statement can be used to create a new table from an existing table
   with a `VECTOR` column. The correct syntax is:
   `CREATE TABLE image_subset AS SELECT image_id, feature_vector FROM images WHERE image_id > 1000`.

4. **What is the primary purpose of the vector_distance() function in Oracle Database 23ai?**
    - [ ] To find the magnitude (length) of a single vector.
    - [ ] To determine the angle between two vectors.
    - [x] To enable similarity searches by measuring the distance between vectors.
    - [ ] To calculate the dot product of two vectors.

   **Explanation:** The `vector_distance()` function enables similarity search by returning the distance between two
   vectors, which is essential for comparing vector embeddings in multidimensional space.

5. **When adding a `VECTOR` column in a table, what additional information can you specify besides the column name?**
    - [ ] The storage size in bytes.
    - [ ] The default value for the column.
    - [ ] The compression algorithm.
    - [x] The number of dimensions and the data type of the vector elements.

   **Explanation:** When adding a `VECTOR` column, you can specify the number of dimensions and the data type of the
   vector elements.