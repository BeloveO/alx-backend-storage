#!/usr/bin/env python3
"""
Class definitions for redis cache
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Methods to handle redid cache
    """
    def __init__(self) -> None:
        """
        Initialize redis cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in redis cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    