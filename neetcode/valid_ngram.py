'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

'''


#  These solution have o(n) TC and O(n) SC
from numpy import sort


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s)!= len(t):
        return False
    
    sdir = {}
    for i in s:
        if i in sdir:
            sdir[i] += 1
        else:
            sdir[i] = 1
            
    tdir = {}
    for i in t:
        if i in tdir:
            tdir[i] += 1
        else:
            tdir[i] = 1
        
    s = set(s)
    for i in s:
        if sdir[i] != tdir.get(i):
            return False
    return True

'or'

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s)!= len(t):
        return False
    
    sdir = {}
    tdir = {}
    for i in range(len(s)):
        sdir[s[i]] = 1 + sdir.get(s[i],0)
        tdir[t[i]] = 1 + tdir.get(t[i],0)
        
    for i in sdir:
        if sdir[i] != tdir.get(i):
            return False
    return True

# I want to optimized the solution with O(1)  SC

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s)!= len(t):
        return False
    
    s = sorted(list(s))
    t = sorted(list(t))
        
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

s = "anagram"
t = "nagaram"
isAnagram(s, t)