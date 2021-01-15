# -*- coding: utf-8 -*-
import unittest
from time import sleep

from mo_cache import MemoryCache


class MemoryCacheTest(unittest.TestCase):

    def test_cache(self):
        cache = MemoryCache()
        cache.set('name', 'Tom')

        sleep(3)
        print(cache.get('name'))
