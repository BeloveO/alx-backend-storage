#!/usr/bin/env python3
"""
Class definitions for redis cache
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Count number of times cache class is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

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

    @count_calls
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
    def get_str(self, key: str) -> str:
        """
        Parametrize cache.get
        """
        data = self.get(key, lambda x: x.decode('utf-8'))
        return data

    def get_int(self, key: str) -> int:
        """
        Parametrize cache.get
        """
        data = self
