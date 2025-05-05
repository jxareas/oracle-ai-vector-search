-- Deleting the table if it exists
DROP TABLE IF EXISTS T1;

-- Creating a table with a vector column with varying dimensions
CREATE TABLE IF NOT EXISTS T1 (
    V VECTOR
);


-- Inserting vector data
INSERT INTO T1 VALUES ('[1.1, 2.7, 3.141592653589793238]'),
    ('[9.34, 0.0, -6.923]'),
    ('[-2.01, 5, -25.8]'),
    ('[-8.2, -5, -1013.6]'),
    ('[7.3]'),
    ('[2.9]'),
    ('[1, 2, 3, 4, 5]');

-- Selecting vector data
SELECT * FROM T1;

-- FORBIDDEN : No comparisons between vectors
-- SELECT V FROM T1 WHERE V = '[2, 9]'
-- THROWS -> ORA-22848: cannot use VECTOR type as comparison key
