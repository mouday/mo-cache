# Mo-Cache

![PyPI](https://img.shields.io/pypi/v/mo-cache.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mo-cache)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mo-cache)
![PyPI - License](https://img.shields.io/pypi/l/mo-cache)


a simple cache lib support memory、file、redis

Github: https://github.com/mouday/mo-cache

## install
 
```bash
pip install mo-cache
```

## demo

```python
from mo_cache import MemoryCache

cache = MemoryCache()

@cache
def foo(a, b):
    return a + b

if __name__ == '__main__':
    foo()

```


继承体系

```python
from abc import ABC

class CacheAbstract(ABC):
    """统一的接口"""
    def set(self, key, value, expire=-1):
        pass

    def get(self, key):
        pass

class CacheDecorator(CacheAbstract):
    """cache 装饰器"""
    
class MemoryCache(CacheDecorator):
    """内存缓存"""

class FileCache(CacheDecorator):
    """文件缓存"""
    
class RedisCache(CacheDecorator):
    """Redis 缓存"""

```
