# Oracle AI Vector Search Queries

## Queries

As of Oracle Database 23ai, queries can contain both a mix of relational data and vector data.

- `INSERT` 
```oraclesqlplus
INSERT INTO T1 VALUES ('[1.1, 2.7, 3.141592653589793238]'),
    ('[9.34, 0.0, -6.923]'),
    ('[-2.01, 5, -25.8]'),
    ('[-8.2, -5, -1013.6]'),
    ('[7.3]'),
    ('[2.9]'),
    ('[1, 2, 3, 4, 5]');
```

Notice, vectors are an array of numbers and can be `NULL`. However, individual vector array element numbers cannot
be `NULL`.

- `SELECT`
```oracle
SELECT * FROM T1;
```

- **NO Comparisons** operations between vectors are allowed

```oracle
SELECT V FROM T1 WHERE V = '[2, 9]';
```

```oracle
SELECT V FROM T1 WHERE V <= '[2, 9]';
```

The former queries both throw `ORA-22848: cannot use VECTOR type as comparison key`