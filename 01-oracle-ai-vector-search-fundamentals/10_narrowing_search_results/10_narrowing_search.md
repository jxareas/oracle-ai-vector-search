# Narrowing Search Results

## Attribute Filtering

Refers to filtering by a column with a `WHERE` clause, as opposed of using an `ORDER BY` clause with `VECTOR_DISTANCE`.

```oracle
SELECT id, vsize, shape, color,
    to_number(vector_distance(vector('[16, 3]'), v, EUCLIDEAN)) AS distance
FROM T2
WHERE id > 30 AND id < 40
ORDER BY vector_distance(vector('[16, 3]'), v, EUCLIDEAN)
FETCH FIRST 3 ROWS ONLY;
```

