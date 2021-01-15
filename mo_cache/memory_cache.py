# -*- coding: utf-8 -*-

from time import time

from .cache_abstract import CacheAbstract


class MemoryCache(CacheAbstract):
    """简单内存cache缓存系统

    参考：https://encrt.com/2016/12/26/python-%E5%86%85%E5%AD%98cache/
    """

    def __init__(self):
        """
        初始化

        数据结构
        {
            key: {
                    value: '',
                    expire_time: ''
                }
        }
        """
        self.data = {}

    def set(self, key, value, expire=-1):
        """
        :param key: 键
        :param value: 值，任何类型
        :param expire: 过期时间，单位：秒， -1为永不过期
        :return:
        """
        if expire > -1:
            expire = time() + expire

        self.data[key] = {
            'value': value,
            'expire_time': expire
        }

    def get(self, key):
        """获取键key对应的值"""
        if key not in self.data:
            return None

        expire = self.data[key]['expire_time']

        if expire == -1 or expire > time():
            return self.data[key]['value']
        else:
            self.data.pop(key)
