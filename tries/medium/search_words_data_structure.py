# https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Design a data structure that supports adding new words and 
# finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure 
# that matches word or false otherwise. word may contain dots '.' 
# where dots can be matched with any letter.


class WordDictionary:
    def __init__(self) -> None:
        self.val = None
        self.children = {}
        self.terminates = False

    def add_word(self, word):
        curr = self
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = WordDictionary()
            curr = curr.children[word[i]]
        curr.terminates = True

    def dfs(self, index, word):
        curr = self

        for i in range(index, len(word)):
            if word[i] == ".":
                for child in curr.children.values():
                    if child.dfs(i + 1, word):
                        return True
                return False
            else:
                if word[i] in curr.children:
                    curr = curr.children[word[i]]
                else:
                    return False
        return curr.terminates

    def search_word(self, word):
        return self.dfs(0, word)

if __name__ == "__main__":
    dictionary = WordDictionary()
    orders = ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
    params = [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

    for order, param in zip(orders, params):
        #print(order, param)
        if order == "addWord":
            print(dictionary.add_word(param[0]))
        if order == "search":
            print(dictionary.search_word(param[0]))