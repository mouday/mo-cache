# -*- coding: utf-8 -*-
from .cache_decorator import CacheDecorator
from .file_cache import FileCache
from .redis_cache import RedisCache
from .memory_cache import MemoryCache


# Factory
def cache_decorator(cache_name, *arg, **kwargs):
    cache_type_mapping = {
        'memory': MemoryCache,
        'file': FileCache,
        'redis': RedisCache,
    }

    cache_class = cache_type_mapping[cache_name]
    return CacheDecorator(cache_class, *arg, **kwargs).cache
