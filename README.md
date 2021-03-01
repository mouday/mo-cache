# Mo-Cache

![PyPI](https://img.shields.io/pypi/v/mo-cache.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mo-cache)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mo-cache)
![PyPI - License](https://img.shields.io/pypi/l/mo-cache)


a simple cache lib support memory、file、redis

Github: https://github.com/mouday/mo-cache

Pypi: https://pypi.org/project/mo-cache

## install
 
```bash
pip install mo-cache
```

## demo

快速开始

```python
from mo_cache import MemoryCache

cache = MemoryCache()


# 此时的key默认是函数名 foo
@cache
def foo(a, b):
    return a + b

if __name__ == '__main__':
    foo()

```

## 更多示例

1、使用装饰器

```python

# 主动设置key, 过期时间单位：秒s
@cache(key='custom_key', expire=30)
def foo(a, b):
    return a + b
```

2、主动设置和获取

```python

cache.set(key='custom_key', value='value', expire=30)

value = cache.get(key='custom_key')
```

MemoryCache, FileCache, RedisCache实现了共同的接口(set/get/call)，

只是构造参数稍有不同

```python

from mo_cache import MemoryCache, FileCache, RedisCache

memory_cache = MemoryCache()

file_cache = FileCache(cache_dir='cache')

redis_cache = RedisCache(redis_url='redis://localhost:6379/0')
```

## 继承体系

```python

class CacheAbstract(object):
    """统一的接口"""
    def set(self, key, value, expire=-1):
        pass

    def get(self, key):
        pass

class CacheDecorator(CacheAbstract):
    """cache 装饰器"""
    def __call__(self, key=None, expire=-1):
        pass
    
class MemoryCache(CacheDecorator):
    """内存缓存"""

class FileCache(CacheDecorator):
    """文件缓存"""
    
class RedisCache(CacheDecorator):
    """Redis 缓存"""

```
