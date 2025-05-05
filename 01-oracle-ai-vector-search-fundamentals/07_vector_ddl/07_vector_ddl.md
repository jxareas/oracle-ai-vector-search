# Vector DDL Operations

**DDL:** Data Definition Language, is a subset of SQL used to define and manage database structures. DDL commands
are used to create, modify and delete database object like tables, indexes and schemas, but not the data inside them.

Common DML Commands:

| Command    | Description                           | Example                                                                       |
|------------|---------------------------------------|-------------------------------------------------------------------------------|
| `CREATE`   | Creates database objects              | ```sql CREATE TABLE employees (id NUMBER PRIMARY KEY, name VARCHAR2(50)); ``` |
| `ALTER`    | Modifies existing objects             | ```sql ALTER TABLE employees ADD (salary NUMBER(10,2)); ```                   |
| `DROP`     | Permanently deletes objects           | ```sql DROP TABLE employees; ```                                              |
| `TRUNCATE` | Removes all rows (faster than DELETE) | ```sql TRUNCATE TABLE employees; ```                                          |
| `RENAME`   | Renames an object (Oracle syntax)     | ```sql RENAME employees TO staff; ```                                         |
| `COMMENT`  | Adds metadata comments                | ```sql COMMENT ON TABLE employees IS 'Company personnel records'; ```         |

## Tables with different `VECTOR` formats

Oracle supports:

- More than one column of `VECTOR` data type.
- `VECTOR` columns with different formats.

We can have

```oracle
CREATE TABLE IF NOT EXISTS T5(
    V1 VECTOR(3, FLOAT32),
    V2 VECTOR(2, FLOAT64),
    V3 VECTOR(1, INT8),
    V4 VECTOR(1, *),
    V5 VECTOR(*, FLOAT32),
    V6 VECTOR(*, *),
    V7 VECTOR
)
```

and similarly we can insert one row with different formats:

```oracle
INSERT INTO T5
VALUES ('[1.1, 2.2, 3.3]',
        '[1.1, 2.2]',
        '[7]',
        '[9]',
        '[1.1, 2.2, 3.3, 4.4, 5.5]',
        '[1.1, 2.2]',
        '[1.1, 2.2, 3.3, 4.4, 5.5, 6.6]');
```

## DDL Operations on Vectors

- Adding vector columns to existing tables
  ```oracle
    ALTER TABLE T6 ADD V2 VECTOR(2, FLOAT32);
  ```
- Deleting vector columns
  ```oracle
  ALTER TABLE T6 DROP COLUMN V2;
  ```

## Prohibited Operations

Oracle has several `VECTOR` data type restrictions, which are that you cannot define `VECTOR` columns in/as:

- External Tables
- IOTs (neither as primary key nor as non-key column)
- Clusters / Cluster Tables
- Global Temp Tables
- (Sub)Partitioning Key
- Primary Key
- Foreign Key
- Unique Constraint
- Check Constraint
- Default Value
- Modify Column
- MSSM Tablespace
- CQN Queries
- Non-vector indexes, such as B-Tree, Bitmap, etc.

Oracle does not support `DISTINCT`, `COUNT DISTINCT`, `ORDER BY`, `GROUP BY`, `JOIN` conditions or comparison operations
with vector columns.
