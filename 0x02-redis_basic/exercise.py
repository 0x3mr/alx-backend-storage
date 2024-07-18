#!/usr/bin/env python3
"""Redis client"""

import redis
import uuid
from typing import Union

class Cache:
    """Cache class to interact with Redis"""
    def __init__(self):
        """Initialize Redis client and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """Generate random key, store data in Redis, and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
