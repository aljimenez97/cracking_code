# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:
    def __init__(self) -> None:
        self.val = None
        self.children = {}
        self.terminates = False

    def insert(self, word: str) -> None:
        if len(word):
            if word[0] in self.children:
                self.children[word[0]].insert(word[1:])
            else:
                self.children[word[0]] = Trie()
                self.children[word[0]].val = word[0]
                self.children[word[0]].insert(word[1:])
        else:
            self.terminates = True

    def search(self, word: str) -> bool:
        if len(word):
            if word[0] in self.children:
                return self.children[word[0]].search(word[1:])
            else:
                return False
        else:
            return self.terminates
        

    def startsWith(self, word: str) -> bool:
        if len(word):
            if word[0] in self.children:
                return self.children[word[0]].startsWith(word[1:])
            else:
                return False
        else:
            return True      

if __name__ == "__main__":
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))   
    print(trie.search("app"))     
    print(trie.startsWith("app")) 
    print(trie.insert("app"))
    print(trie.search("app")) 