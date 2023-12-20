#!/usr/bin/env python3
"""
Lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    List all documents
    """
    if not mongo_collection:
        return []
    return list(mongo_collection)
