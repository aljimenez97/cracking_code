
class Bucket:
    def __init__(self):
        self.bucket = []
    def put(self, original_key, value):
        found = False
        for i, elem in enumerate(list(self.bucket)):
            key = elem[0]
            if key == original_key:
                self.bucket[i] = (original_key, value)
                found = True
                break
        if not found:
            self.bucket.append((original_key, value))
    def get(self, original_key):
        found = list(filter(lambda x: x[0] == original_key, self.bucket))
        return found[0][1] if len(found) else -1
    def remove(self, original_key):
        if len(self.bucket):
            indexes = [i for i, (key, _) in enumerate(self.bucket) if key == original_key]
            try:
                self.bucket.pop(indexes[0])
            except:
                pass


class HashMap:
    def __init__(self):
        self.limit = 1000
        self.hash_table = [Bucket() for i in range(self.limit)]
    def put(self, key, value):
        hash_key = key % self.limit
        self.hash_table[hash_key].put(key, value)
    def get(self, key):
        hash_key = key % self.limit
        return self.hash_table[hash_key].get(key)
    def remove(self, key):
        hash_key = key % self.limit
        self.hash_table[hash_key].remove(key)


if __name__ == "__main__":
    myHashMap = HashMap()
    print(myHashMap.remove(3)) 
