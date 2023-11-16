from time import time
from collections import OrderedDict


def cached(cache):
    def wrapper(func):
        return cache(func)
    return wrapper


class SimpleCache:
    def __init__(self, func):
        self.func = func
        self.cache_dict = {}

    def __call__(self, *args, **kwargs):
        value = self.cache_dict.get((self.func.__name__, args), None)
        if value:
            return value
        result = self.func(*args, **kwargs)
        self.cache_dict[(self.func.__name__, args)] = result
        return self.cache_dict


class FIFOCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache_dict = OrderedDict()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            value = self.cache_dict.get((func.__name__, args), None)
            if value:
                return value
            if len(self.cache_dict) == self.max_size:
                self.cache_dict.popitem(last=False)
            result = func(*args, **kwargs)
            self.cache_dict[(func.__name__, args)] = result
            return self.cache_dict[(func.__name__, args)]
        return wrapper


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache_dict = {}

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            value = self.cache_dict.get((func.__name__, args), None)
            if value:
                # update last request time
                self.cache_dict[(func.__name__, args)][1] = time()
                return value[0]
            if len(self.cache_dict) >= self.max_size:
                sorted_cache_dict = sorted(self.cache_dict.items(),
                                           key=lambda x: x[1][1])
                del self.cache_dict[sorted_cache_dict[0][0]]
            result, request_time = func(*args, **kwargs), time()
            self.cache_dict[(func.__name__, args)] = [result, request_time]
            return self.cache_dict[(func.__name__, args)][0]
        return wrapper


class TTLCache:
    def __init__(self, max_size, ttl):
        self.max_size = max_size
        self.ttl = ttl
        self.cache_dict = {}

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            value = self.cache_dict.get((func.__name__, args), None)
            if value and value[2] > time():
                # update last request time
                self.cache_dict[(func.__name__, args)][1] = time()
                # update live time
                self.cache_dict[(func.__name__, args)][2] = time() + self.ttl
                return value[0]

            for key, value in list(self.cache_dict.items()):
                if value[2] <= time():
                    del self.cache_dict[key]
            if len(self.cache_dict) >= self.max_size:
                sorted_cache_dict = sorted(self.cache_dict.items(),
                                           key=lambda x: x[1][1])
                del self.cache_dict[sorted_cache_dict[0][0]]

            result = func(*args, **kwargs)
            self.cache_dict[(func.__name__, args)] = [result,
                                                      time(),
                                                      time() + self.ttl]
            return self.cache_dict[(func.__name__, args)][0]
        return wrapper
