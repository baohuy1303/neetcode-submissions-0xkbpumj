class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None

class LRU:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_tail(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node

        node.next = self.tail
        node.prev = prev
        self.size += 1

    def unlink(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

        self.size -= 1

    def evict_lru(self):
        node = self.head.next
        self.unlink(self.head.next)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freqs = defaultdict(LRU) # freq -> lru/linkedlist
        self.keys = {} # key -> node
        self.min_freq = 1

    def move_buckets(self, node):
        old_bucket = self.freqs[node.freq]
        old_bucket.unlink(node)
        if old_bucket.size == 0:
            if self.min_freq == node.freq:
                self.min_freq += 1
            del self.freqs[node.freq]

        node.freq += 1

        new_bucket = self.freqs[node.freq]
        new_bucket.add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        node = self.keys[key]
        self.move_buckets(node)
    
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.value = value
            self.move_buckets(node)
            return

        node = Node(key, value)
        if self.capacity == len(self.keys):
            min_bucket = self.freqs[self.min_freq]
            evict_node = min_bucket.evict_lru()
            del self.keys[evict_node.key]

            if min_bucket.size == 0:
                del self.freqs[self.min_freq]
        
        self.keys[key] = node
        self.min_freq = 1
        self.freqs[1].add_to_tail(node)
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)