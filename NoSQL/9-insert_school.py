#!/usr/bin/env python3
"""Insert a new document into a MongoDB collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: key-value pairs representing the document.

    Returns:
        The new document's _id.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
