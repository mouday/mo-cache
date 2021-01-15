# -*- coding: utf-8 -*-
from hashlib import md5

from .cache_abstract import CacheAbstract
from .logger import logger
import pickle


class CacheDecorator(object):
    """cache 装饰器"""

    def __init__(self, cache_class, *arg, **kwargs):
        if not issubclass(cache_class, CacheAbstract):
            raise Exception('cache_class must is subclass of CacheAbstract')

        self.cache_instance = cache_class(*arg, **kwargs)

    def cache(self, key=None, expire=-1, params_sign=True):
        """
        :param key:
            如果没有指定cache_key, cache_key = 模块名.方法名.方法参数md5值
            如果指定了cache_key, cache_key = 指定的cache_key.方法参数md5值

        :param expire: 缓存时间 秒

        :param params_sign: 参数指纹，方法参数的md5值 加入到 cache_key 不同参数可以单独缓存
        :return:
        """

        def wrapper(func):

            # 默认key
            if key is None or callable(key):
                cache_key = func.__module__ + '.' + func.__name__
            else:
                cache_key = key

            def inner_wrapper(*args, **kwargs):

                # 增加参数签名
                if params_sign is True:
                    params = pickle.dumps(args) + pickle.dumps(kwargs)
                    inner_cache_key = cache_key + '.' + md5(params).hexdigest()
                else:
                    inner_cache_key = cache_key

                logger.debug('cache_key: %s', inner_cache_key)

                value = self.cache_instance.get(inner_cache_key)

                if not value:
                    value = func(*args, **kwargs)
                    self.cache_instance.set(inner_cache_key, value, expire)

                return value

            return inner_wrapper

        # 可以不写函数括号
        if callable(key):
            return wrapper(key)

        return wrapper
