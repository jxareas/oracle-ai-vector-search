# Other Distance Functions

Previously, we talked about some of the other distance functions used with `VECTOR_DISTANCE`, such as Manhattan,
Euclidean, Cosine and Dot Product.

In this section, we'll introduce some of the other distance functions that are synonymous with those.

- `L1_DISTANCE(v1, v2)`: **Manhattan Distance**
- `L2_DISTANCE(v1, v2)`: **Euclidean Distance**
- `COSINE_DISTANCE(v1, v2)`: **Cosine Distance**
- `INNER_PRODUCT(v1, v2)`: **Dot Product**

Example:

```oracle
-- VECTOR DISTANCE WITH COSINE DISTANCE METRIC
SELECT *
FROM t2
ORDER BY VECTOR_DISTANCE(vector('[16, 4, 2]'), v, COSINE)
    FETCH FIRST 2 ROWS ONLY;

-- COSINE DISTANCE
SELECT *
FROM t2
ORDER BY COSINE_DISTANCE(vector('[16, 4, 2]'), v)
    FETCH FIRST 2 ROWS ONLY;
```