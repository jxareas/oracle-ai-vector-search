-- Convert a string to vector
SELECT to_vector('[34.6, 77.8]', 2, float32) FROM dual;
SELECT vector('[1.1, 2.2, 3.3]', 3, float32) FROM dual;

-- Convert a vector into string or CLOB
SELECT vector_serialize(vector('[1.1, 2.2, 3.3]', 3, float32)) FROM dual;
SELECT from_vector(vector('[1.1, 2.2, 3.3]', 3, float32)) FROM dual;

-- Calculate the distance from the origin to the vector (vector norm)
SELECT vector_norm(vector('[4, 3]', 2, float32)) FROM dual;

-- Get number of dimensions of a vector
SELECT vector_dimension_count(vector('[34.6, 77.8]', 2, float64)) FROM dual;

-- Get storage format of the vector
SELECT vector_dimension_format(vector('[34.6, 77.8]', 2, float64)) FROM dual;