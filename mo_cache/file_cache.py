# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os
import pickle
from time import time

from .cache_decorator import CacheDecorator


class FileCache(CacheDecorator):
    """
    文件缓存
    参考：
    https://zhuanlan.zhihu.com/p/25110164
    """

    # 默认的缓存文件夹
    default_cache_dir = 'cache'

    def __init__(self, cache_dir=None):
        self.cache_dir = cache_dir or self.default_cache_dir

    def create_cache_dir(self):
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def get_cache_filename(self, key):
        return os.path.join(self.cache_dir, '%s.cache' % key)

    def set(self, key, value, expire=-1):
        self.create_cache_dir()

        if expire > -1:
            expire = time() + expire

        obj = {
            'value': value,
            'expire_time': expire
        }

        with open(self.get_cache_filename(key), 'wb') as f:
            pickle.dump(obj, f)

    def get(self, key):
        cache_filename = self.get_cache_filename(key)

        if not os.path.exists(cache_filename):
            return None

        with open(cache_filename, 'rb') as f:
            obj = pickle.load(f)

        expire = obj['expire_time']

        if expire == -1 or expire > time():
            return obj['value']
