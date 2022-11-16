from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cache_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.cache_dict.get(key, None)
        if value is not None:
            self.cache_dict.move_to_end(key)
        else:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        if self.cache_dict.get(key, None):
            self.cache_dict[key] = value
            self.cache_dict.move_to_end(key)
        elif len(self.cache_dict) >= self.capacity:
            self.cache_dict.popitem(last=False)
            self.cache_dict[key] = value
        else:
            self.cache_dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cache_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.cache_dict.get(key, None)
        if value is not None:
            self.cache_dict.move_to_end(key)
        else:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        if self.cache_dict.get(key, None):
            self.cache_dict.move_to_end(key)
        elif len(self.cache_dict) >= self.capacity:
            self.cache_dict.popitem(last=False)
        self.cache_dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
