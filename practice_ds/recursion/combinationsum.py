from copy import deepcopy
def combinedsum(arr,ind,target,res,ans):
    if ind >= len(arr):
        if target == 0:
            ans.append(deepcopy(res))
        return ans
    
    
    if arr[ind] <= target:
        res.append(arr[ind])
        ans = combinedsum(arr,ind,target-arr[ind],res,ans)
        res.pop()
    
    ans = combinedsum(arr,ind+1,target,res,ans)
    return ans
    

arr = [2,3,6,7]
target = 7

combinedsum(arr,0,target,[],[])
