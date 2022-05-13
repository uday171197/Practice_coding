


from copy import deepcopy


def combinationSum(arr,n,i,t,res,ans):
    if i >= n:
        if  t == 0:
            r = deepcopy(res)
            ans.append(r)
        return 
    if arr[i] <= t:
        res.append(arr[i])
        combinationSum(arr,n,i,t-arr[i],res,ans)
        res.pop()
    
    combinationSum(arr,n,i+1,t,res,ans)
    return ans


candidates = [2,3,6,7]
target = 7
n = len(candidates)
combinationSum(candidates,n,0,target,[],[])

