# Other Vector Functions - Questions

1. Which of the following SQL statements demonstrates the correct usage of the `to_vector()` function in Oracle Database 23ai?
   - [ ] `SELECT to_vector([34.6, 77.8], 2, float32) FROM dual`
   - [ ] `SELECT to_vector('34.6, 77.8', 2, float32) FROM dual`
   - [x] `SELECT to_vector('[34.6, 77.8]', 2, float32) FROM dual`
   - [ ] `SELECT to_vector('34.6, 77.8, 2, float32) FROM dual`

2. What is the primary purpose of the `VECTOR_SERIALIZE()` function in Oracle Database 23ai?

   - [x] To convert a vector to a string or CLOB data type
   - [ ] To calculate the distance between two vectors
   - [ ] To create a new vector from a string representation
   - [ ] To determine the number of dimensions in a vector

3. Which of the following actions will result in an error when using `VECTOR_DIMENSION_COUNT()` in Oracle Database 23ai?

   - [ ] Providing a vector with duplicate values for its components
   - [ ] Calling the function on a vector that has been created with `to_vector()`
   - [ ] Using a vector with a data type that is not supported by the function
   - [x] Providing a vector with a dimensionality that exceeds the specified dimension count

4. Which SQL statement correctly retrieves the format of the numbers stored in the vector `[34.6, 77.8, 9, 10]` using the `vector_dimension_format()` function in Oracle Database 23ai?

   - [ ] `SELECT vector_dimension_format('INT8') FROM dual;`
   - [x] `SELECT vector_dimension_format(vector('[34.6, 77.8, 9, 10]', 4, INT8)) FROM dual;`
   - [ ] `SELECT vector_dimension_format(34.6, 77.8, 9, 10) FROM dual`
   - [ ] `SELECT vector_dimension_format(34.6, 77.8, 9, 10, 3 '1') FROM dual`

5. What is the primary purpose of the `VECTOR_NORM()` function in Oracle Database 23ai?

   - [ ] To determine the number of dimensions in a vector
   - [ ] To calculate the Euclidean distance between two vectors
   - [ ] To convert a vector to a string representation
   - [x] To return the magnitude or length of a vector