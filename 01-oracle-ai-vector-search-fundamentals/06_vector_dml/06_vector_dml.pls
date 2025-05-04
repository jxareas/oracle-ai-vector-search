-- Creating a table with a VECTOR column
CREATE TABLE IF NOT EXISTS T2(
    ID NUMBER NOT NULL,
    NAME VARCHAR(32),
    V1 VECTOR,
    PRIMARY KEY (ID)
);

-- Inserting into the table with a vector column
INSERT INTO T2
VALUES (1, 'A', '[1.1]') ,
    (2, 'B', '[2.2]')
    ,
    (3, 'C', '[3.3]')
    ,
    (4, 'D', '[4.4]')
    ,
    (5, 'E', '[5.5]');

-- Counting the number of rows inserted
SELECT COUNT(*)
FROM T2;

-- Creating a table with several vector columns
-- NOTE : Normalized tables will most likely have only one vector column
CREATE TABLE IF NOT EXISTS T3 (
    ID NUMBER NOT NULL,
    NAME VARCHAR2(32),
    V1 VECTOR,
    V2 VECTOR,
    V3 VECTOR,
    PRIMARY KEY (ID),
)

-- Inserting several vectors in several vector columns
INSERT INTO T3
VALUES (1,
        'One',
        '[2.3, 4.5, 0.1]',
        '[1.1]',
        '[4.981, -3.6]')

-- Creating a table with a vector column with fixed format and number of elements
CREATE TABLE IF NOT EXISTS T4 (
    V VECTOR(3, FLOAT32)
)

