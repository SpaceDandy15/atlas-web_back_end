#!/usr/bin/env python3
"""Update topics of a school document by name."""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object.
        name (str): the name of the school to update.
        topics (list): list of strings representing the new topics.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
