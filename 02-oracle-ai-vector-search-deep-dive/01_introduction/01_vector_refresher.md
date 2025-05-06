# Vector Refresher

## `VECTOR` Data Type

Introduced in Oracle Database 23ai is a new data type called `VECTOR`, which allows us to store vector embeddings
alongside other business data, in the same table or in separate tables within the database.

Such an example is:

```oracle
CREATE TABLE HOUSE_FOR_SALE
(
    HOUSE_ID     NUMBER,
    PRICE        NUMBER,
    CITY         VARCHAR2(400),
    HOUSE_PHOTO  BLOB,
    HOUSE_VECTOR VECTOR
);
```

| Possible Declaration            | Explanation                                                                                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `VECTOR`                        | Vectors can have an arbitrary number of dimensions and formats.                                                               |
| `VECTOR(*,*)`                   | `VECTOR` and `VECTOR(*,*)` are equivalent.                                                                                    |
| `VECTOR (num_of_dimensions, *)` | Vectors must all have the specified number of dimensions.                                                                     |
| `VECTOR (num_of_dimensions)`    | Vectors must all have the specified number of dimensions                                                                      |
| `VECTOR (*, dimension_format)`  | Vectors can have an arbitrary number of dimensions and specified dimension_format (`INT8`, `FLOAT32`,`FLOAT64`, or `BINARY`). |

## Vector Embeddings

- Embeddings are a technique of representing data as vectors in a way that captures meaningful information.
- Such data might be a word, phrase, sentence, paragraph or one or more paragraphs.
- Embeddings make it easy for computers to understand the relationships between pieces of text.

Vector embeddings can be generated outside the database using 3rd party embedding models or inside the local Database
23ai by downloading pre-trained embedding models, converting them into ONNX format (if they are not) & importing the
ONNX format models into Database 23ai.

23ai SQL functions allow us to chunk and generate embeddings: `VECTOR_CHUNK`, `VECTOR_EMBEDDING`.
23ai PL/SQL packages to generate embeddings: `DBMS_VECTOR`, `DBMS_VECTOR_CHAIN`.

