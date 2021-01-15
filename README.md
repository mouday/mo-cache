# Mo-Cache

a simple cache lib support memory、file、redis


## install
 
```bash
pip install Mo-Cache
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

