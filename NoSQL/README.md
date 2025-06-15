NoSQL Project - README
General Overview
What is NoSQL?
NoSQL stands for "Not Only SQL" and refers to a broad class of database management systems designed to handle large volumes of unstructured or semi-structured data. Unlike traditional relational databases, NoSQL databases provide flexible schemas and scale horizontally.

Difference Between SQL and NoSQL
SQL databases use structured query language and have fixed schemas, enforcing ACID properties to ensure reliable transactions.

NoSQL databases are schema-less or have flexible schemas and support different data models such as document, key-value, wide-column, or graph. They often prioritize scalability and performance over strict ACID compliance.

What is ACID?
ACID stands for Atomicity, Consistency, Isolation, Durability — a set of properties guaranteeing reliable processing of database transactions. Traditional SQL databases fully support ACID, while many NoSQL databases relax some of these properties for scalability and speed.

What is Document Storage?
Document storage is a NoSQL database model where data is stored in documents, typically in JSON-like formats (e.g., BSON in MongoDB). Documents contain fields and values, allowing for nested and complex data structures without fixed schemas.

Types of NoSQL Databases
Document Stores (e.g., MongoDB, CouchDB) — store data as JSON-like documents.

Key-Value Stores (e.g., Redis, DynamoDB) — store data as key-value pairs.

Wide-Column Stores (e.g., Cassandra, HBase) — store data in tables with dynamic columns.

Graph Databases (e.g., Neo4j) — store data as nodes and relationships.

Benefits of NoSQL Databases
Flexible schemas allow easy evolution of data models.

Designed for horizontal scaling and high availability.

Handle large volumes of diverse and unstructured data.

Typically provide better performance on distributed systems.

How to Query Information from a NoSQL Database
NoSQL databases provide query languages or APIs tailored to their data models. For example, MongoDB uses a rich query syntax based on JSON-like documents, allowing filtering, projection, sorting, and aggregation.

How to Insert/Update/Delete Information from a NoSQL Database
NoSQL databases provide commands or methods for data manipulation. In MongoDB:

Insert: db.collection.insertOne() or insertMany()

Update: db.collection.updateOne(), updateMany()

Delete: db.collection.deleteOne(), deleteMany()

How to Use MongoDB
MongoDB is a popular document-oriented NoSQL database. It stores data in BSON documents within collections. You interact with MongoDB using:

The mongosh shell for manual queries.

Drivers in various programming languages like Python (via PyMongo).

MongoDB supports CRUD operations, aggregation pipelines, indexing, and replication.

