# -*- coding: utf-8 -*-
import os
import pickle
from hashlib import md5
from time import time

from .cache_abstract import CacheAbstract


class FileCache(CacheAbstract):
    """delete、clear 删除动作较为危险，不实现具体方法

    参考：
    https://zhuanlan.zhihu.com/p/25110164
    """

    def __init__(self, cache_dir='cache'):
        self.cache_dir = cache_dir
        self._create_cache_dir()

    def _create_cache_dir(self):
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def _get_cache_filename(self, key):
        return os.path.join(self.cache_dir, '%s.cache' % md5(key.encode()).hexdigest())

    def set(self, key, value, expire=-1):

        if expire > -1:
            expire = time() + expire

        obj = {
            'value': value,
            'expire_time': expire
        }

        with open(self._get_cache_filename(key), 'wb') as f:
            pickle.dump(obj, f)

    def get(self, key):
        cache_filename = self._get_cache_filename(key)

        if not os.path.exists(cache_filename):
            return None

        with open(cache_filename, 'rb') as f:
            obj = pickle.load(f)

        expire = obj['expire_time']

        if expire == -1 or expire > time():
            return obj['value']
