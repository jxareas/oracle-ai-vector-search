-- DEMO : Finding Nearest Vectors

-- Creating a simple vector by using the vector constructor
SELECT VECTOR('[0, 0]');

-- Specifying a vector's dimension and format
SELECT VECTOR('[0, 5]', 2, FLOAT32);

-- Computing the Euclidean vector distance
SELECT TO_NUMBER(VECTOR_DISTANCE(
                 VECTOR('[0, 0, 5]'),
                 VECTOR('[10, 0, 8]'),
                 EUCLIDEAN
                 )) AS EUCLIDEAN_DISTANCE;

SELECT TO_NUMBER(VECTOR_DISTANCE(
                 VECTOR('[0, 0, 5]'),
                 VECTOR('[10, 0, 8]'),
                 MANHATTAN
                 )) AS MANHATTAN_DISTANCE;

-- SELECT TO_NUMBER(VECTOR_DISTANCE(
--                  VECTOR('[0, 2, 2]'),
--                  VECTOR('[10, 0]'),
--                  MANHATTAN
--                  )) AS MANHATTAN_DISTANCE;
-- THROWS ERROR -> VECTOR DISTANCE IS NOT SUPPORTED FOR VECTORS WITH DIFFERENT DIMENSION COUNTS (3, 2)
