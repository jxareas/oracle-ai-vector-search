# Vector Indexing Refresher

## Vector Index

A vector index is a specialized data structure designed for similarity searches in high-dimensional vector spaces.
It helps accelerate similarity searches by using techniques such as clustering, partitioning and neighbor graphs to
group similar vectors together to reduce the search space.

### Why do we need a vector index?

Enable fast similarity searches across large vector datasets. Without indexes, searching would require a comparison
against every vector. Hence, indexing drastically reduces the search space.

Indexing improves query performance and enables efficient approximate nearest neighbors (ANN) searches.

There are two types of vector indexes:

- **HNSW** (Hierarchical Navigable Small World / In-Memory Neighbor Graph): Stored in memory (SGA). Very efficient for
  vector similarity searches. Uses a layered hierarchical organization. Is it considered **THE BEST CHOICE** when
  data fits in memory.

```oracle
CREATE
VECTOR INDEX CUSTOM_HNSW_IDX
ON MY_TABLE (VECTOR_COLUMN)
ORGANIZATION
INMEMORY NEIGHBOR GRAPH
DISTANCE COSINE
WITH TARGET ACCURACY 90
PARAMETERS (TYPE HNSW, NEIGHBORS 40, EFCONSTRUCTION 500)
```

HNSW Parameters:

* **`NEIGHBORS`**: Maximum number of connections per vector (1-2048).
* **`EFCONSTRUCTION`**: Number of closest vector candidates considered during each step of HNSW index creation (
  1-65535). A higher value improves accuracy but can increase creation time.
* **`TARGET ACCURACY`**: Desired accuracy percentage (0-100). A value of 90% means the algorithm aims for 90% accuracy
  while balancing speed.


- **IVF** (Inverted File Flat / Neighbor Partition): It's a partition-based approach. Balances search quality with
  speed, while being better suited for larger datasets. It supports DML operations.

### Vector Pool

Memory in the System Global Area (SGA) designed to HNSW vector indexes and associated metadata. It also speeds up
operations related with IVF indexes. It is configured using the `VECTOR_MEMORY_SIZE` parameter.
This parameter can be modified at either:

- CDB level (Container database)
- PDB level (Pluggable database)

```oracle
ALTER SYSTEM SET VECTOR_MEMORY_SIZE=1 G SCOPE = BOTH;
```

```oracle
CREATE
VECTOR INDEX CUSTOM_IVF_IDX
ON MY_TABLE (VECTOR_COLUMN)
ORGANIZATION
NEIGHBOR PARTITIONS
DISTANCE COSINE
WITH TARGET ACCURACY 95
PARAMETERS (TYPE IVF, NEIGHBOR PARTITIONS 10);
```

IVF Parameters:

* **`NEIGHBOR PARTITIONS`**: Number of centroid partitions. Increasing it allows the algorithms to search more
  partitions, leading to higher accuracy.
* **`SAMPLES_PER_PARTITION`**: Training sample size.
* **`TARGET ACCURACY`**: Desired accuracy percentage (0-100). A value of 95% means the algorithm aims for 95% accuracy
  while balancing speed.

### Comparison

| Feature        | In-Memory Neighbor Graph (HNSW)                                                                                                     | Neighbor Partition (IVF)                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Method         | Constructs a multi-layered hierarchical graph, connecting vectors based on their proximity. Employs a navigational search algorithm | Divides the vector space into partitions (clusters) based on centroids. Limits searches to a subset of relevant partitions |
| Accuracy       | Generally higher accuracy, especially when the entire index fits in memory                                                          | Sacrifices some accuracy for speed. Accuracy can degrade over time due to DML operations                                   |
| Performance    | Excels in performance when the index fits in memory. Can be affected if the index size exceeds available memory                     | Designed for speed and can handle larger datasets. Less dependent on memory availability.                                  |
| DML Operations | Allowed on the indexed table after index creation                                                                                   | Supported, making it suitable for dynamic datasets. Frequent DML operations can reduce accuracy                            |
| Memory         | High; the entire index is stored in memory                                                                                          | Lower; relies on partitioning to reduce search space                                                                       |
| RAC            | Not supported                                                                                                                       | Supported; benefits from setting up a vector pool on each instance                                                         |

## Using Vector Indexes

- Must use `APPROX` or `APPROXIMATE` keywords.
- Distance function must match the index. If the distance metric used in a query differs from the one specified during
  the index creation, the system performs an exact match instead of using the vector index.
- All vectors must have the same dimension.

```oracle
SELECT *
FROM MY_TABLE
WHERE VECTOR_DISTANCE(VECTOR_COLUMN, :QUERY_VECTOR, COSINE) < 0.5
    FETCH APPROXIMATE FIRST 10 ROWS ONLY;
```

## Best Practices

- Size the vector pool appropriately.
- Use HNSW when data fits in memory.
- Use IVF for larger datasets.
- Match distance metrics with the embedding model.
- Monitor index accuracy.
- Regular maintenance for IVF indexes.
- Consider rebuilding indexes when accuracy drops.