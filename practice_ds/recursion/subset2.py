'''
This solution have o(2**n) * log(2**n) * n

we ahve fornd all the possible subset and add into set and then convert each value in list
'''

from copy import deepcopy
def subset2(arr,ind,res,ans):
    
    if ind >= len(arr):
        ans.add(tuple(res))
        return
    
    res.append(arr[ind])
    subset2(arr,ind+1,res,ans)
    res.pop()
    subset2(arr,ind+1,res,ans)
    return ans

arr = [1,2,2]
ans = subset2(arr,0,[],set())
[list(i) for i in ans]
# method2

def subset2(arr,ind,res,ans):
    if ind >= len(arr):
        if res not in ans:
            ans.append(deepcopy(res))
        return
    
    res.append(arr[ind])
    subset2(arr,ind+1,res,ans)
    res.pop()
    subset2(arr,ind+1,res,ans)
    return ans

arr = [1,2,2]
ans =   (arr,0,[],[])


'''
optimized solution where time coplexity is O(2**n)* k 

space complexity is O(2**n) * O(k)
'''

def subset2(arr,ind,res,ans):
    print(res)
    for i in range(ind,len(arr)):
        if i> ind and arr[i] == arr[i-1]:
            continue
        res.append(arr[i])
        subset2(arr,i+1,res,ans)
        res.pop()
    return ans

arr = [1,2,2]
ans = subset2(arr,0,[],[])