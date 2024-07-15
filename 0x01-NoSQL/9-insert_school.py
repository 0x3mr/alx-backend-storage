#!/usr/bin/env python3
"""
a Python function that inserts a new document in a collection based on kwargs:
"""

def insert_school(mongo_collection, **kwargs):
    """
    Prototype: def insert_school(mongo_collection, **kwargs):
    Return: the new _id
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id