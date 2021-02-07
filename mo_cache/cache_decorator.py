# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import pickle
from functools import wraps
from hashlib import md5

from .cache_abstract import CacheAbstract
from .logger import logger


class CacheDecorator(CacheAbstract):
    """cache 装饰器"""

    def set(self, key, value, expire=-1):
        raise NotImplementedError()

    def get(self, key):
        raise NotImplementedError()

    def __call__(self, key=None, expire=-1):
        """
        缓存装饰器
        :param key:
            如果没有指定cache_key, cache_key = 模块名.方法名.方法参数md5值
            如果指定了cache_key, cache_key = 指定的cache_key.方法参数md5值

        :param expire: 缓存时间 秒；默认-1，永久缓存

        :return: object
        """

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # 默认key
                cache_key = self.get_cache_key(key, func, *args, **kwargs)

                logger.info('cache_key: %s', cache_key)

                value = self.get(cache_key)

                if not value:
                    value = func(*args, **kwargs)
                    self.set(key=cache_key, value=value, expire=expire)

                return value

            return wrapper

        # 可以不写函数括号
        if callable(key):
            return decorator(key)

        return decorator

    def _get_md5(self, text):
        """获取md5"""
        return md5(text).hexdigest()

    def _get_params_sign(self, *args, **kwargs):
        """获取参数唯一值"""
        params = pickle.dumps(args) + pickle.dumps(kwargs)
        return self._get_md5(params)

    def _get_func_name(self, func):
        """获取函数的名称"""
        return func.__module__ + '.' + func.__name__

    def get_cache_key(self, key_or_func, func, *args, **kwargs):
        """获取缓存key"""
        cache_key = key_or_func

        # 默认key
        if key_or_func is None or callable(key_or_func):
            cache_key = self._get_func_name(func)

        # 增加参数签名
        cache_key = cache_key + '.' + self._get_params_sign(*args, **kwargs)

        return cache_key
