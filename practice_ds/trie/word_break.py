class TrieNode:
    def __init__(self):
        self.links = [None]*26
        self.flag = False

class Trie:
    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        return TrieNode()
    
    def _containkey(self,ch):
        return ord(ch)-ord('a')
    
    def insert(self,word):
        wordnode = self.root
        for ch in word:
            index = self._containkey(ch)
            if not wordnode.links[index]:
                wordnode.links[index] = self.getNode()
                print(ch,'----wordnode.links-----',wordnode.links)
            wordnode = wordnode.links[index]
        wordnode.flag = True
        
    def search(self,word):
        wordnode = self.root
        for i in range(len(word)):
            print('not found',word[i])
            index = self._containkey(word[i])
            if not wordnode.links[index]:
                return False
            if wordnode.flag:
                print('word found')
                wordnode = self.root 
            elif i == len(word)-1:
                return wordnode.flag
            else:
                wordnode = wordnode.links[index]
        
    
s = "leetcode"
wordDict = ["leet","code"]

i = 0
words = set(wordDict)
start_points = [0]

while i < len(s):
    for element in start_points:
        if s[element:i + 1] in words:
            start_points.append(i + 1)
            break
    i += 1
start_points[-1] == len(s)

            
            
           
        
            
        
        