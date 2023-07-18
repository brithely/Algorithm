"""
2022.11.16
https://leetcode.com/problems/lru-cache/
Medium
"""

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


"""
2023.07.18
https://leetcode.com/problems/lru-cache/
Medium
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.order_dict = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if self.order_dict.get(key) is not None:
            self.order_dict.move_to_end(key)
        return self.order_dict.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        if self.order_dict.get(key) is not None:
            self.order_dict.move_to_end(key)
        elif len(self.order_dict) >= self.capacity:
            self.order_dict.popitem(last=False)
        self.order_dict[key] = value
        
