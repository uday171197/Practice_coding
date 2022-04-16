'''
Printing all the subsequence which having sum value
'''


def subsequenceOfSum(arr,s,ind,res):
    if ind >= len(arr):
        if sum(res) == s:
            print(res)
        return
    res.append(arr[ind])
    subsequenceOfSum(arr,s,ind+1,res)
    res.pop()
    subsequenceOfSum(arr,s,ind+1,res)
    

    
arr = [1,2,1]
subsequenceOfSum(arr,2,0,[])

#                                     or

def subsequenceOfSum(arr,s,ind,res,sumvaue):
    if ind >= len(arr):
        if sumvaue == s:
            print(res)
        return
    res.append(arr[ind])
    sumvaue+=arr[ind]
    subsequenceOfSum(arr,s,ind+1,res,sumvaue)
    res.pop()
    sumvaue-=arr[ind]
    subsequenceOfSum(arr,s,ind+1,res,sumvaue)
    
subsequenceOfSum(arr,2,0,[],0)


'''
I am trying to print only one subsequence which having sum value.

'''

def oneSubsequenceOfSum(arr,s,ind,res,sumvaue):
    if ind >= len(arr):
        if sumvaue == s:
            print(res)
            return True # return true if first subsequence are found 
        return False # false if condition not satisfied
    res.append(arr[ind])
    sumvaue+=arr[ind]
    if  oneSubsequenceOfSum(arr,s,ind+1,res,sumvaue): 
        return True 
    res.pop()
    sumvaue-=arr[ind]
    if oneSubsequenceOfSum(arr,s,ind+1,res,sumvaue):
        return True
    return False
oneSubsequenceOfSum(arr,2,0,[],0)


'''
Print the count of subsequence which have sum is s
'''

def countSubSeq(arr,n,ind,s,res,sumvalue,count):
    if ind >= n:
        if sumvalue == s:
            count +=1
            return count
        return count
    
    res.append(arr[ind])
    sumvalue+=arr[ind]
    count = countSubSeq(arr,n,ind+1,s,res,sumvalue,count)
    
    res.pop()
    sumvalue-=arr[ind]
    
    count = countSubSeq(arr,n,ind+1,s,res,sumvalue,count)
    
    return count
        
countSubSeq(arr,3,0,2,[],0,0)

# second method

def countSubSeq(arr,n,ind,s,res,sumvalue):
    if ind >= n:
        if sumvalue == s:
            return 1
        return 0
    
    res.append(arr[ind])
    sumvalue+=arr[ind]
    l = countSubSeq(arr,n,ind+1,s,res,sumvalue)
    
    res.pop()
    sumvalue-=arr[ind]
    
    r = countSubSeq(arr,n,ind+1,s,res,sumvalue)
    
    return l+r
        
countSubSeq(arr,3,0,2,[],0)

