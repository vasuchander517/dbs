import datetime


class Cache:

    def __init__(self):
        self.cache = {}
        self.max_cache_size = 25

    def __contains__(self, key):
        return key in self.cache


def get(self, key):
    if key not in self.cache and len(self.cache) >= self.max_cache_size:
        self.cache[key] = {}  # need to replace with service call.
    return self.cache[key]


def update(self, key, value):
    if key not in self.cache and len(self.cache) >= self.max_cache_size:
        self.remove_oldest()
    self.cache[key] = {'date_accessed': datetime.datetime.now(),
                       'value': value}


def remove_oldest(self):
    oldest_entry = None
    for key in self.cache:
        if oldest_entry is None:
            oldest_entry = key
        elif self.cache[key]['date_accessed'] < self.cache[oldest_entry]['date_accessed']:
            oldest_entry = key
    self.cache.pop(oldest_entry)


def size(self):
    return len(self.cache)
