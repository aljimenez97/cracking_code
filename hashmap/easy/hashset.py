
class Bucket:
    def __init__(self):
        self.bucket= []
    def update(self, key):
        # Do not allow duplicates
        if key not in self.bucket:
            self.bucket.append(key)
    def get(self, key):
        return key in self.bucket
    def remove(self, key):
        try:
            self.bucket.remove(key)
        except:
            pass

class HashSet:
    def __init__(self):
        self.limit = 100
        self.hash_table = [Bucket() for i in range(self.limit)]
    def add(self, key):
        hash_key = key%self.limit
        self.hash_table[hash_key].update(key)
    def remove(self, key):
        hash_key = key%self.limit
        self.hash_table[hash_key].remove(key)
    def contains(self, key):
        hash_key = key%self.limit
        return self.hash_table[hash_key].get(key)

if __name__ == "__main__":
    myHashSet = HashSet()
    print(myHashSet.add(1))      
    print(myHashSet.add(2))      
    print(myHashSet.contains(1))
    print(myHashSet.contains(3))
    print(myHashSet.add(2))
    print(myHashSet.contains(2))
    print(myHashSet.remove(2)) 
    print(myHashSet.contains(2))