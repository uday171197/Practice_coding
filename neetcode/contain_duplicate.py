
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

'''

from sqlalchemy import true


def duplicate_contain(s):
    if len(s) != len(set(s)):
        return True
    return False


'optimized solution '

def duplicate_contain(s):
    st = set()
    for i in s:
        if i in st:
            return True
        st.add(i)
    return False


s= [1,1,2,3,1]
duplicate_contain(s)
    