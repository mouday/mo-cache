# -*- coding: utf-8 -*-

import pickle

from redis import Redis

from .cache_abstract import CacheAbstract


class RedisCache(CacheAbstract):
    def __init__(self, redis_url):
        self.redis = Redis.from_url(redis_url)

    def set(self, key, value, expire=-1):
        if expire == -1:
            expire = None

        value = pickle.dumps(value)
        self.redis.set(key, value, expire)

    def get(self, key):
        value = self.redis.get(key)

        if value:
            return pickle.loads(value)
