# its have O(2**n)*n time complexity 

def powerset(s,res,ind):
    if ind >= len(s):
        return 
    print(res)
    
    for i in range(ind+1,len(s)):
        res += s[i]
        powerset(s,res,i)
        res = res[:-1]
    return

powerset('abc','',-1)

def powerset(s,res,ind):
    if ind >= len(s):
        return 
    print(res)
    
    for i in range(ind+1,len(s)):
        res.append(s[i])
        powerset(s,res,i)
        res.pop()
    return

powerset([1,2,3],[],-1)