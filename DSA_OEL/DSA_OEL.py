class Node:
    def __init__(self, k, v):
        """initialize a doubly linked list"""
        self.key = k
        self.value = v
        self.next = None
        self.prev = None


class LRU_cache_:
    def __init__(self, capacity):
        """Initialize LRU cache with given capacity"""
        self.capacity = capacity
        # Dictionary to store key-node pairs for quick lookup
        self.dic = dict()
        # Create sentinel nodes for the doubly linked list
        self.head = Node(0, 0)  # Head sentinel
        self.tail = Node(0, 0)  # Tail sentinel
        # Connect sentinels to form an empty doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head
        # Counters for cache statistics
        self.miss = 0
        self.total_count = 0

    def __str__(self):
        """String representation of the cache for debugging purposes"""
        result = []
        current = self.head.next
        while current.next:
            result.append((current.key, current.value))
            current = current.next
        return str(result)

    def add_(self, node):
        """Add a node to the end of the doubly linked list"""
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p

    def remove_(self, node):
        """Remove a node from the doubly linked list"""
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def get_(self, key):
        """Retrieve the value associated with the key from the cache"""
        self.total_count += 1
        if key in self.dic:
            # If key exists, move the corresponding node to the end of the list (recently used)
            n = self.dic[key]
            self.remove_(n)
            self.add_(n)
            return n.value
        else:
            # If key is not found in the cache, increment miss counter and return -1
            self.miss += 1
            return -1

    def put_(self, key, value):
        """Insert or update a key-value pair in the cache"""
        self.total_count += 1
        if key in self.dic:
            # If key exists, update the value and move the node to the end of the list
            node = self.dic[key]
            node.value = value
            self.remove_(node)
            self.add_(node)
        else:
            self.miss += 1
            # If key doesn't exist, create a new node and add it to the end of the list
            node = Node(key, value)
            self.add_(node)
            self.dic[key] = node

        if len(self.dic) > self.capacity:
            # If the cache exceeds its capacity, evict the least recently used node (from the front)
            node = self.head.next
            self.remove_(node)
            del self.dic[node.key]


# Example usage of the LRU_cache class
cache = LRU_cache_(50)

# Filling the full cache using keys 0-49
for i in range(50):
    cache.put_(i, i)

# Retrieve the odd-numbered keys
print("Odd-numbered keys from 1-50")
for i in range(1, 50, 2):
    print(cache.get_(i), end=', ')
print('\nCache after retrieving odd-numbered keys'), print(cache)

# Insert a key-value pair and observe the cache state
cache.put_(2, 2)
print("Inserting (2,2) key-value pair"), print(cache)

# Fill the cache with prime-numbered keys
for i in range(3, 98):
    for j in range(2, i):
        if not i % j:
            break
    else:
        cache.put_(i, i)

# Display the final cache state and statistics
print("Cache after filling prime-numbered keys"), print(cache)
print("Total Count:", cache.total_count)
print("Miss Count:", cache.miss)
miss_rate = (cache.miss / cache.total_count) * 100
print("Miss Rate:", miss_rate)
