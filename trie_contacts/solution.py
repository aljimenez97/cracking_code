class Trie():
    def __init__(self, value):
        self.value = value
        self.terminates = False
        self.children = {}
        self.num_descendants = 0
        
    def add_word(self, word):
        self.num_descendants += 1
        if len(word) == 0:
            self.terminates = True
        elif word[0] in self.children:
            self.children[word[0]].add_word(word[1:])
        else:
            self.children[word[0]] = Trie(word[0])
            self.children[word[0]].add_word(word[1:])
            
            
    def count_branches(self):
        count = 0
        
        stack = []
        stack.append(self)
        
        while len(stack):
            popped = stack.pop()
            if popped.terminates:
                count += 1
            stack.extend(popped.children.values())

        return count

    def search_prefix(self, prefix):
        if len(prefix) == 0:
            return self.num_descendants
        elif prefix[0] in self.children:
            return self.children[prefix[0]].search_prefix(prefix[1:])
        else:
            return 0

def contacts(queries):
    trie = Trie(None)
    for q in queries:
        command, opt = q.split(" ")
        if command == "add":
            trie.add_word(opt)
        elif command == "find":
            print(trie.search_prefix(opt))

if __name__ == "__main__":
    queries =["add s", "add ss", "add sss", "add ssss", "add sssss", "find s", "find ss", "find sss", "find ssss", "find sssss", "find ssssss"]
    contacts(queries)