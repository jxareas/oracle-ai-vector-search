-- CREATING AND TRUNCATING TABLE
CREATE TABLE IF NOT EXISTS T3 (
    ID NUMBER PRIMARY KEY,
    V VECTOR(3, *),
    SHAPE_COLOR VARCHAR2(100)
);
TRUNCATE TABLE T3;
-- INSERTING DATA INTO T3
INSERT INTO T3 VALUES (1,'[1.1, 2.7, 7.141592653589793238]', 'Red'),
    (2,'[1.2, 2.9, 3.141592653589793238]', 'Red'),
    (3,'[1.3, 2.7, 3.141592653589793238]', 'Red'),
    (4,'[1.4, 2.7, 3.141592653589793238]', 'Blue'),
    (5,'[1.9, 3.7, 3.141592653589793238]', 'Red'),
    (6,'[1.11, 2.2, 3.141592653589793238]', 'Red'),
    (7,'[1.12, 2.9, 3.14]', 'Orange');
------------------------------------------------------------------------------------------------------------------------
-- L1 DISTANCE
-- The L1 Distance function is equivalent to using the Vector Distance function with the Manhattan distance metric.
SELECT ID FROM T3
ORDER BY VECTOR_DISTANCE(V, TO_VECTOR('[1.1, 2.7, 7.141592653589793238]'), MANHATTAN)
FETCH FIRST 5 ROWS ONLY;

SELECT ID FROM T3
ORDER BY L1_DISTANCE(V, TO_VECTOR('[1.1, 2.7, 7.141592653589793238]'))
FETCH FIRST 5 ROWS ONLY;
------------------------------------------------------------------------------------------------------------------------
-- L2 DISTANCE
-- The L2 Distance function is equivalent to using the Vector Distance function with the Euclidean distance metric.
SELECT ID FROM T3
ORDER BY VECTOR_DISTANCE(V, TO_VECTOR('[1.1, 2.7, 7.141592653589793238]'), EUCLIDEAN)
FETCH FIRST 5 ROWS ONLY;

SELECT ID FROM T3
ORDER BY L2_DISTANCE(V, TO_VECTOR('[1.1, 2.7, 7.141592653589793238]'))
FETCH FIRST 5 ROWS ONLY;
------------------------------------------------------------------------------------------------------------------------
-- COSINE DISTANCE
-- The Cosine Distance function is equivalent to using the Vector Distance function with the Cosine distance metric.
SELECT ID FROM T3
ORDER BY VECTOR_DISTANCE(V, TO_VECTOR('[1.1, 2.7, 7.141592653589793238]'), COSINE)
FETCH FIRST 5 ROWS ONLY;

SELECT ID FROM T3
ORDER BY COSINE_DISTANCE(V, TO_VECTOR('[1.1, 2.7, 7.141592653589793238]'))
FETCH FIRST 5 ROWS ONLY;
------------------------------------------------------------------------------------------------------------------------
-- INNER PRODUCT
-- The Inner Product function is equivalent to NEGATING the Vector Distance function with the Dot distance metric.
SELECT ID FROM T3
ORDER BY -1 * VECTOR_DISTANCE(V, TO_VECTOR('[1.1, 2.7, 7.141592653589793238]'), DOT) -- NEGATED DOT PRODUCT
FETCH FIRST 5 ROWS ONLY;

SELECT ID FROM T3
ORDER BY INNER_PRODUCT(V, TO_VECTOR('[1.1, 2.7, 7.141592653589793238]')) -- DOT PRODUCT
FETCH FIRST 5 ROWS ONLY;