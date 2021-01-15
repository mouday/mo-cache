# -*- coding: utf-8 -*-
from abc import ABC


class CacheAbstract(ABC):
    """统一的接口"""
    def set(self, key, value, expire=-1):
        pass

    def get(self, key):
        pass
