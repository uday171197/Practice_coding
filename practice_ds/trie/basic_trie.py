from numpy import True_


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
        # print('ch',ch)
        return ord(ch) - ord('a')
    
    def insert(self,word):
        wordnode = self.root
        for ch in word.lower():
            iscontainkey = self._containKey(ch)
            if not  wordnode.links[iscontainkey]: 
                wordnode.links[iscontainkey] = self.getNode()
            wordnode = wordnode.links[iscontainkey]
        wordnode.flag = True
        
        
    def search(self,word):
        wordnode = self.root
        for ch in word.lower():
            iscontainkey = self._containKey(ch)
            # print(iscontainkey,wordnode.links[iscontainkey])
            if wordnode.links[iscontainkey]:
                wordnode = wordnode.links[iscontainkey]
            else:
                return False
        return wordnode.flag
    
    def startwith(self,prefix):
        wordnode = self.root
        for ch in prefix.lower():
            iscontainkey = self._containKey(ch)
            # print(iscontainkey,wordnode.links[iscontainkey])
            if wordnode.links[iscontainkey]:
                wordnode = wordnode.links[iscontainkey]
            else:
                return False
        return True
    
    
if __name__ == '__main__':
    t = Trie()
    word = 'apples'
    t.insert(word)
    isfound= t.search('apples')
    if isfound:
        print('The word found')
    else:
        print('Don"t have word found')
        
    isfound= t.startwith('pa')
    if isfound:
        print('The word found as prefix')
    else:
        print('Don"t have word found prefix')
    