# Mo-Cache

![PyPI](https://img.shields.io/pypi/v/mo-cache.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mo-cache)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mo-cache)
![PyPI - License](https://img.shields.io/pypi/l/mo-cache)


a simple cache lib support memory、file、redis


## install
 
```bash
pip install mo-cache
```

## demo
```python
from mo_cache import cache_decorator

cache = cache_decorator('memory')

@cache
def foo(a, b):
    return a + b

if __name__ == '__main__':
    foo()
```

