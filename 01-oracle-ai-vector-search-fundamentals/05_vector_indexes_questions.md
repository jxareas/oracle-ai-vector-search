# Oracle Vector Search and Memory Management - Test Questions

1. **What is the approximate memory requirement (in GB) for an In-memory Neighbor Graph index with 1,000,000 rows, each
   represented by a vector with 1024 dimensions and a vector format size of 4 bytes?**
    - [ ] About 1.9 GB
    - [ ] About 7.4 GB
    - [x] About 5.0 GB
    - [ ] About 3.7 GB

   **Explanation:** The formula for estimating the in-memory size of In-memory Neighbor Graph indexes is: 1.3 * Size of
   vector format * number of dimensions * number of rows. Applying the values from the question: 1.3 * 4 * 1024 *
   1,000,000 = 5,324,800,000 bytes, which is approximately 5.0. The constant 1.3 accounts for overhead and graph layers.

2. **What is the primary function of a Vector Index in Oracle Database 23ai?**
    - [ ] To convert traditional relational data into vector representations.
    - [ ] To calculate the dot product of two vectors.
    - [x] To efficiently search for vectors that are similar to a given query vector.
    - [ ] To store vector data directly on disk.

   **Explanation:** Vector Indexes are specialized indexing data structures designed to optimize vector search
   operations. These indexes employ techniques like clustering, partitioning, and neighbor graphs to significantly
   reduce the search space, enabling fast and efficient retrieval of similar vectors.

3. **Where is the Vector Pool located within the Oracle Database 23ai architecture?**
    - [ ] In the Program Global Area (PGA).
    - [ ] In the Redo Log Buffer.
    - [ ] In the Database Buffer Cache.
    - [x] In the System Global Area (SGA).

   **Explanation:** Vector Pool is a component within the System Global Area (SGA). The SGA is a shared memory region
   that holds data and control information for an Oracle Database instance.

4. **What is the significance of the VECTOR_MEMORY_SIZE parameter in Oracle Database 23ai?**
    - [ ] It sets the precision of floating-point numbers used in vector computations.
    - [ ] It determines the dimensionality of vectors that can be created.
    - [ ] It limits the maximum number of vectors that can be stored in the Vector Pool.
    - [x] It defines the maximum memory usage allowed for the Vector Pool in the SGA.

   **Explanation:** `VECTOR_MEMORY_SIZE` is a parameter used to control the size of the Vector Pool. The parameter can
   be set at both the database (`CDB`) and pluggable database (`PDB`) levels. The value set for this parameter dictates
   the maximum amount of SGA memory that can be allocated to the Vector Pool, effectively limiting its size.

5. **Which of the following is a recommended approach when there is insufficient RAM to accommodate large vector
   indexes?**
    - [ ] Reduce the dimensionality of the vectors.
    - [ ] Disable the Vector Pool in the SGA.
    - [x] Utilize Inverted File Flat (IVF) indexes.
    - [ ] Increase the size of the Redo Log Buffer.

   **Explanation:** It is recommended to use Inverted File Flat (IVF) indexes as an alternative when available RAM is
   insufficient to handle large vector indexes. IVF indexes leverage both the buffer cache and disk storage, making them
   more suitable for scenarios with RAM constraints.