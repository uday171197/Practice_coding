
from uuid import getnode


class TrieNode:
    def __init__(self) -> None:
        self.link = [None]*26
        self.word = False
class Trie:
    
    def __init__(self) -> None:
        self.root = self.getNode()
    
    def getNode(self):
        return TrieNode()
    
    def _iscontain(self,ch):
        return ord(ch)-ord('a')
    
    def insertWord(self,word):
        wordnode = self.root
        for ch in word.lower():
            indx = self._iscontain(ch)
            if not wordnode.link[indx]:
                wordnode.link[indx] = self.getNode()
            wordnode = wordnode.link[indx]
        wordnode.word = True
        
    def searchWord(self,word):
        wordnode = self.root
        for ch in word.lower():
            indx = self._iscontain(ch)
            if wordnode.link[indx]:
                wordnode = wordnode.link[indx]
            else:
                return False 
        return wordnode.word
        
    def startWith(self,pre):
        wordnode = self.root
        for ch in pre.lower():
            indx = self._iscontain(ch)
            if wordnode.link[indx]:
                wordnode = wordnode.link[indx]
            else:
                return False
        return True

t = Trie()

t.insertWord('apple')
t.searchWord('appl')
t.startWith('appe')

