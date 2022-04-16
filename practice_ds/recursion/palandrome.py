
def reverseArray(s,i=0):
    length = len(s)
    if i > length/2:
        return True
    if s[i] != s[length-1-i]:
        return False
    return reverseArray(s,i+1)
    
s = 'abad'
reverseArray(s)