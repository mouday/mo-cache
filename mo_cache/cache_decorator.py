# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from functools import wraps

from .utils import get_func_name
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
            如果没有指定key, cache_key = 模块名.方法名
            如果指定了key, cache_key = 指定的key

        :param expire: 缓存时间 秒；默认-1，永久缓存

        :return: object
        """

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # 默认key
                cache_key = self.get_cache_key(key_or_func=key, func=func)

                logger.info('cache_key: %s', cache_key)

                value = self.get(key=cache_key)

                if not value:
                    value = func(*args, **kwargs)
                    self.set(key=cache_key, value=value, expire=expire)

                return value

            return wrapper

        # 可以不写函数括号
        if callable(key):
            return decorator(key)

        return decorator

    def get_cache_key(self, key_or_func, func):
        """获取缓存key, 可以被重写"""

        # 默认key
        if key_or_func is None or callable(key_or_func):
            cache_key = get_func_name(func)
        else:
            cache_key = key_or_func

        return cache_key
