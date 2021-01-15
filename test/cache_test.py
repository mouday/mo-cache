# -*- coding: utf-8 -*-

import unittest
from mo_cache import cache_decorator


class CacheTest(unittest.TestCase):
    def test_factory(self):

        cache = cache_decorator('memory')

        @cache
        def foo(a, b):
            return a + b

        @cache()
        def foo2(a, b):
            return a + b

        @cache('key')
        def foo3():
            return None

        @cache('key', params_sign=False)
        def foo4():
            return None

        foo(1, 1)
        foo(1, 1)
        foo(1, 2)
        foo2(1, 2)
        foo2(1, 2)
        foo2(1, 1)

        foo3()
        foo3()

        foo4()
        foo4()
