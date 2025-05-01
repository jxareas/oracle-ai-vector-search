# Finding the Closest Vectors

## Exact Similarity Search

Calculates the query vector distance to all other vectors. Also called _flat search_.
This gives us:

- Most accurate results
- Perfect search quality
- But involes potentially significant search times

Using Euclidean Distance:

```oracle
SELECT docID
FROM vector_tab
ORDER BY VECTOR_DISTANCE(embedding, :query_vector, EUCLIDEAN)
    FETCH EXACT FIRST 10 ROWS ONLY;
```

Using Euclidean Squared Distance:

```oracle
SELECT docID
FROM vector_tab
ORDER BY VECTOR_DISTANCE(embedding, :query_vector)
    FETCH FIRST 10 ROWS ONLY;
```

## Approximate Similarity Search

Approximate similarity search uses vector indexes. To use vector indexes, it is required to have enabled the
vector pool in the SGA.

These type of searches:

- Can be more efficient than exact similarity search.
- Can be less accurate
- Uses target accuracy

Remember, we have two types of vector indexes:

- HNSW (Hierarchical Navigable Small World) Index

```oracle
-- Creating a HNSW vector index
CREATE
VECTOR INDEX galaxies_hnsw_idx 
       ON galaxies(embedding)
       ORGANIZATION INMEMORY NEIGHBOR GRAPH
       DISTANCE COSINE
WITH TARGET ACCURACY 95;

SELECT name
FROM galaxies
WHERE name <> 'NGC1073'
ORDER BY VECTOR_DISTANCE(embedding, TO_VECTOR('[0, 1, 1, 0, 0]'), COSINE)
    FETCH APPROXIMATE FIRST 3 ROWS ONLY;
```

- IVF (Inverted File Flat) Index

```oracle
-- Creating a HNSW vector index
CREATE
VECTOR INDEX galaxies_ivf_idx 
       ON galaxies(embedding)
       ORGANIZATION NEIGHBOR PARTITIONS
       DISTANCE COSINE
WITH TARGET ACCURACY 95;

SELECT name
FROM galaxies
WHERE name <> 'NGC1073'
ORDER BY VECTOR_DISTANCE(embedding, TO_VECTOR('[0, 1, 1, 0, 0]'), COSINE)
    FETCH APPROXIMATE FIRST 3 ROWS ONLY;
```

## Multi-Vector Similarity Search

