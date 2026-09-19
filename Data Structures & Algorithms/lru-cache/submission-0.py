class LRUCacheNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.left = LRUCacheNode()
        self.right = LRUCacheNode()
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        node = self.hashMap[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self._remove(self.hashMap[key])
        
        node = LRUCacheNode(key, value)
        self.hashMap[key] = node
        self._insert(node)

        if len(self.hashMap) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.hashMap[lru.key]