#!/usr/bin/env python3
"""Function that lists all documents in a collection"""
def list_all(mongo_collection):
    """Lists all documents in the given MongoDB collection"""
    if mongo_collection is None:
        """If the collection is None, return an empty list"""
        return []
    return list(mongo_collection.find())
