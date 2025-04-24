-- Creating a table with several vector columns
CREATE TABLE IF NOT EXISTS T5 (
    V1 VECTOR(3, FLOAT32),
    V2 VECTOR(2, FLOAT64),
    V3 VECTOR(1, INT8),
    V4 VECTOR(1, *),
    V5 VECTOR(*, FLOAT32),
    V6 VECTOR(*, *),
    V7 VECTOR,
);

-- Inserting several values
INSERT INTO VALUES ('[1.1, 2.2, 3.3]',
    '[1.1, 2.2]',
    '[7]',
    '[9]',
    '[1.1, 2.2, 3.3, 4.4, 5.5]',
    '[1.1, 2.2]',
    '[1.1, 2.2, 3.3, 4.4, 5.5, 6.6]');

-- Creating a table T6 without any vector column
CREATE TABLE IF NOT EXISTS T6(
    ID NUMBER NOT NULL,
    NAME VARCHAR2(32),
    PRIMARY KEY(ID)
);

-- Adding a vector column to table T6
ALTER TABLE T6
    ADD V1 VECTOR;
-- Adding another vector column to table T6
ALTER TABLE T6
    ADD V2 VECTOR(2, FLOAT32);

-- Deleting a vector column
ALTER TABLE T6 DROP COLUMN V2;

-- Deleting the whole table
DROP TABLE IF EXISTS T6;

-- Using the CTAS (Create table as Select) operation
CREATE TABLE IF NOT EXISTS T7 AS SELECT * FROM T3;