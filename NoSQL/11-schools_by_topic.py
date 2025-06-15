#!/usr/bin/env python3
"""Module to find schools by topic."""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school documents that have a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): the topic to search for.

    Returns:
        List of documents matching the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
