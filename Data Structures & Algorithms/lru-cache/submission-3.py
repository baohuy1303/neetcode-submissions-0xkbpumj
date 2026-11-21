class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def unlink(self, key):
        node = self.keys[key]

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
        return

    def put_to_front(self, key):
        node = self.keys[key]

        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node

        node.next = self.tail
        node.prev = prev

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        self.unlink(key)
        self.put_to_front(key)

        return self.keys[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].value = value
            self.unlink(key)
            self.put_to_front(key)
            return

        if len(self.keys) == self.capacity:
            least_recent = self.head.next
            self.unlink(least_recent.key)
            del self.keys[least_recent.key]

        self.keys[key] = Node(key, value)
        self.put_to_front(key)
        return
