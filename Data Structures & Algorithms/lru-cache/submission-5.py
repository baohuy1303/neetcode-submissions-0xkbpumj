class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head

    def unlink(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def put_to_front(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node

        node.prev = prev
        node.next = self.tail

    def evict_lru(self):
        node = self.head.next
        self.unlink(node)

        del self.keys[node.key]

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        node = self.keys[key]
        self.unlink(node)
        self.put_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.value = value
            self.unlink(node)
        else:
            if self.capacity == len(self.keys):
                self.evict_lru()
            node = Node(key, value)
            self.keys[key] = node

        self.put_to_front(node)
        return



