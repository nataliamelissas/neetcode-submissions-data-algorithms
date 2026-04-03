class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.time = 0
        self.capacity = capacity
        self.last_accessed_dict = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.last_accessed_dict[key] = self.time
            self.time += 1
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.last_accessed_dict[key] = self.time
        self.time += 1
        if len(self.cache) > self.capacity:
            earliest = self.time
            for k,v in self.last_accessed_dict.items():
                if v < earliest:
                    earliest = v
                    kd = k
            del self.cache[kd]
            del self.last_accessed_dict[kd]
        
