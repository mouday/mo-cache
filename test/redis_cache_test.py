# -*- coding: utf-8 -*-
import unittest
from time import sleep

from mo_cache import RedisCache


class RedisCacheTest(unittest.TestCase):

    def test_cache(self):
        url = 'redis://localhost:6379/0'
        cache = RedisCache(url)

        cache.set('name', {'name': 'Tom', 'age': 33})

        print(cache.get('name'))

        cache.set('age', 23, 1)
        sleep(2)
        print(cache.get('age'))

        @cache
        def foo(name):
            print('foo inner')
            return 'foo' + name

        print(foo('name'))
        print(foo('name'))
        print(foo('jack'))
        print(foo('steve'))
