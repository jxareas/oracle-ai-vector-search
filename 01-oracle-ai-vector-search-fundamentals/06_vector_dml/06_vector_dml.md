# Vector DML Operations

**DML:** Data Manipulation Language, is a subset of SQL used to insert, update, delete and retrieve data inside of a
database. It operates the records within a database table.

Common DML Commands:

1. `SELECT`
    ```sql
    SELECT * FROM employees;
   ```
2. `INSERT`
    ```sql
    INSERT INTO employees (id, name, salary);
   ```
3. `UPDATE`
    ```sql
    SELECT * FROM employees;
   ```
4. `DELETE`
    ```sql
    SELECT * FROM employees;
   ```

## Creating a Table with a `VECTOR` column

`VECTOR` is a new data type introduced in Oracle Database 23ai in order to support vector search. The definition can
include:

- The number of dimensions
- Format (`BINARY`, `INT8`, `FLOAT32`, `FLOAT64` or not specified)

Either one of those is optional when defining the vector column.

Example:

```oracle
CREATE TABLE my_vectors
(
    id        NUMBER,
    embedding VECTOR
);
```

Notice, we're not defining either the number of dimensions, or the format.

```oracle
CREATE TABLE my_vectors
(
    id        NUMBER,
    embedding VECTOR(768, INT8)
)
```

For this vector, each stored vector must have 768 dimensions and be formatted as an `INT8`.

### Declaration Formats and Explanations

> `VECTOR`

Vectors can have an arbitrary number of dimensions and format.

> `VECTOR(*, *)`

Vectors can have an arbitrary number of dimensions and format. `VECTOR` and `VECTOR(*, *)` are equivalent.

> `VECTOR(n_dim, *)`

Vectors must all have the specified number of dimensions or an error is thrown. Every vector will have its dimension
stored without format modification. Is also equivalent to `VECTOR(n_dim)`.

> `VECTOR(*, dimension_element_format)`

Vectors can have an arbitrary number of dimensions, but their format will be up-converted or down-converted to the
specified `dimension_element_format`: `INT8`, `FLOAT32` or `FLOAT64`.

## Vector DML

Vector DML allows us to insert vectors into tables, just as shown:

```oracle
CREATE TABLE galaxies (
    id NUMBER,
    name VARCHAR2(50),
    doc VARCHAR2(500),
    embedding VECTOR
);

INSERT INTO galaxies VALUES (
    1,
    'M31',
    'Messier 31 is a barred spiral galaxy in the Andromeda constellation which has a lot of barred spiral galaxies.',
    '[0,2,2,0,0]'
);

INSERT INTO galaxies VALUES (
    9,
    'NGC1073',
    'NGC 1073 is a barred spiral galaxy in Cetus constellation.',
    '[0,1,1,0,0]'
);

COMMIT;
```

Likewise, we can directly update or delete vectors in the table:

```oracle
UPDATE T2
    SET V1 = '[2, 9]'
    WHERE ID = 2
COMMIT;
```

```oracle
DELETE FROM T2
    WHERE ID IN (1, 3);
COMMIT;
```

You can also load data using 'SQL Loader'.