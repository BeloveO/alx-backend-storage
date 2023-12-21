#!/usr/bin/env python3
"""
Class definitions for redis cache
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float, None]:
        """
        Get data from redis cache
        """
        data = self._redis.get(key)
        if data is not None and fn is not None and callable(fn):
            return fn(data)
        return data
