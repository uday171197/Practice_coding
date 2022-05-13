
from copy import deepcopy

def uniquesubset(arr,n,i,res,ans):
    if i > n:
        return
    r = deepcopy(res)
    ans.append(r)
    for j in range(i,n):
        if j!=i and arr[j]==arr[j-1]:
            continue
        res.append(arr[j])
        uniquesubset(arr,n,j+1,res,ans)
        res.pop()
    return ans
    
    



N = 3
arr = [1,1,3]
uniquesubset(arr,N,0,[],[])