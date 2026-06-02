class MyHashMap:

    def __init__(self):
        # 1. Initialize a list of N empty lists (buckets) 
        # Using a prime number (like 1000) for size helps reduce collisions
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        # 2. Get the index using hash function (key % size)
        index = key % self.size
        # 3. Access the specific bucket at that index
        bucket = self.buckets[index]
        # 4. Search through the bucket for the key:  
        for i, (k, v) in enumerate(bucket):
            # If found: update the existing value and return
            if k == key:
                bucket[i] = (key, value)
                return
        # 5. If loop finishes and key wasn't found:
            # Append the new (key, value) tuple to the bucket
        bucket.append((key, value))
        

    def get(self, key: int) -> int:
        # 6. Get the index using hash function
        index = key % self.size
        # 7. Access the specific bucket at that index
        bucket = self.buckets[index]
        # 8. Loop through the bucket to find the key:
        for i, (k, v) in enumerate(bucket):
            # If pair[0] == key: 
            if k == key:
                # return pair[1]
                return v
        # 9. If we finish the loop without returning: return -1
        return -1

    def remove(self, key: int) -> None:
        # 10. Get the index using hash function
        index = key % self.size
        # 11. Access the specific bucket
        bucket = self.buckets[index]
        # 12. Loop through the bucket to find the key:
        for i, (k, v) in enumerate(bucket):
            # If pair[0] == key: remove that tuple from the bucket
            if k == key:
                del bucket[i]
                return




        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)