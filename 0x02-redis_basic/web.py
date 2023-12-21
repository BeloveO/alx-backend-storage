#!/usr/bin/env python3
"""
Use requests module to obtain HTML content of a URL
"""
import redis
import requests
from datetime import timedelta


def get_page(url: str) -> str:
    """
    Return html content of a url
    """
    if url is None or len(url.strip()) == 0:
        return ''
    redis_store = redis.Redis()
    res_key = 'result:{}'.format(url)
    req_key = 'count:{}'.format(url)
    result = redis_store.get(res_key)
    if result is not None:
        redis_store.incr(req_key)
        return result
    result = requests.get(url).content.decode('utf-8')
    redis_store.setex(res_key, timedelta(seconds=10), result)
    return result
