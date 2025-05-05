# Other Vector Functions

Other common vector functions include:

- Vector Constructors
- Vector Serializers
- Vector Norm
- Vector Dimension Count
- Vector Dimension Format

## Vector Constructors

`TO_VECTOR` is a function which converts a string or `CLOB` into a vector.

Example:

```oracle
SELECT TO_VECTOR('[34.6, 77.8]', 2, FLOAT32)
FROM dual;
```

This is similar to using the `VECTOR()` constructor:

```oracle
SELECT VECTOR('[34.6, 77.8]', 2, FLOAT32);
```

## Vector Serializers

Converts a vector a string or `CLOB`.

Example:

```oracle
SELECT VECTOR_SERIALIZE(VECTOR('[1.1, 2.2, 3.3]', 3, FLOAT32));
```

This is synonymous to using the function `FROM_VECTOR`.

```oracle
SELECT FROM_VECTOR(VECTOR('[1.1, 2.2, 3.3]', 3, FLOAT32));
```

## Vector Norm

Returns the Euclidean norm of a vector. That is, the distance from the origin to the vector.

Example:

```oracle
SELECT VECTOR_NORM(VECTOR('[4, 3]', 2, FLOAT32));
```

## Vector Dimension Count

Returns a vector's dimensions.

Example:

```oracle
SELECT VECTOR_DIMENSION_COUNT(VECTOR('[44, 21, 298]'));
```

## Vector Dimension Format

Returns the storage format of a vector.

Example:

```oracle
SELECT VECTOR_DIMENSION_FORMAT(VECTOR('[44, 23, 298.2]'));
```

