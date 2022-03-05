class TrieNode:
    def __init__(self):
        self.links = [None]*26
        self.flag = False

class Trie:

    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        return TrieNode()
    
    def _containKey(self,ch):
        return ord(ch)-ord('a')

    def insert(self, word: str) -> None:
        wordnode = self.root
        for ch in word:
            index = self._containKey(ch)
            if not wordnode.links[index]:
                wordnode.links[index] = self.getNode()
            wordnode = wordnode.links[index]
        
        wordnode.flag = True

    def search(self, word: str) -> bool:
        wordnode = self.root
        for ch in word:
            index = self._containKey(ch)
            if not wordnode.links[index]:
                return False
            wordnode = wordnode.links[index]
        return wordnode.flag

    def startsWith(self, prefix: str) -> bool:
        wordnode = self.root
        for ch in prefix:
            index = self._containKey(ch)
            if not wordnode.links[index]:
                return False
            wordnode = wordnode.links[index]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie =  Trie()
trie.insert("apple")
trie.search("apple")  # return True
trie.search("app")    #return False
trie.startsWith("app") #return True
trie.insert("app")
trie.search("app")