## Finding the Nearest Vectors

## Vector Constructor

The vector constructor is a function which allows us to create vectors without having to store them inside the column
of a table.

These are useful for learning purposes, and are generally used with a small number of dimensions (as most embedding
models contain thousands of different dimensions).

It also allows us to specify the vector values.

- Dimension is OPTIONAL.
- Format is OPTIONAL.

Example:

```oracle
SELECT VECTOR('[0, 0]');
```

```oracle
SELECT VECTOR('[1, 2, 3]', 3, INT8);
```

## Vector Distance Operand

The Vector Distance Operand allows us to use the main function: **`VECTOR_DISTANCE``**, which takes two vectors as
parameters (metric is optional, defaults to `cosine`).

Distances available:

- cosine distance
- l1 distance
- l2 distance
- inner product

The vector distance function is used to perform a similarity search.

### Vector Distance Metrics

#### Euclidean and Euclidean Squared Distances

The **Euclidean Distance** refers to the straight-line distance between two vectors, computed by using the
Pythagorean theorem.
It is sensitive to both:

- Vector Size
- Vector Direction

#### Cosine Similarity

One of the most widely used similarity metrics, specially in natural language processing. The **smaller the angle, the
more similar** two vectors are considered.

#### Dot Product Similarity

Multiplies the size of each vector by the cosine of their angle, which is also equivalent to the sum of the vector
coordinates.

**Larger means more similar, smaller means less similar**.

#### Manhattan Distance

Useful for describing uniform grids:

- City Blocks
- Power Grids
- Chessboard

Faster than the Euclidean metric.

#### Hamming Similarity

Describes where vector dimensions differ.

Binary Vectors:

- Number of bits which require change to match

Compares the position of each bit in the sequence and are used for network error detection.

#### Jaccard


Examples of `VECTOR_DISTANCE`:

```oracle
SELECT TO_NUMBER(VECTOR_DISTANCE(
                 VECTOR('[0, 0]'),
                 VECTOR('[10, 0]'),
                 EUCLIDEAN
                 )) AS DISTANCE
```

## Shorthand Operators

- `<->` **Euclidean Distance Operator**
  - Equivalent to `L2_DISTANCE(expr1, expr2)` or `VECTOR_DISTANCE(expr1, expr2, EUCLIDEAN)`.
- `<=>` **Cosine Distance Operator**
  - Equivalent to `COSINE_DISTANCE(expr1, expr2)` or `VECTOR_DISTANCE(expr1, expr2, COSINE)`.
- `<#>` **Negative Dot Product Operator**
  - Equivalent to `-1*INNER_PRODUCT(expr1, expr2)` or `VECTOR_DISTANCE(expr1, expr2, DOT)`.
- 