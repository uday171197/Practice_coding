


from copy import deepcopy


def combinationSum2(arr,n,i,t,res,ans):
    if i >= n:
        if t == 0 and res not in ans:
            r = deepcopy(res)
            ans.append(r)
        return 
    
    # for j in range(i,n):
    #     if j!=i and arr[j]==arr[j-1]:
    #         continue
    #     res.append(arr[j])
    #     combinationSum2(arr,n,i+1,t,res,ans)
    #     res.pop()
    # print(res)
    if arr[i] <= t:
        res.append(arr[i])
        combinationSum2(arr,n,i+1,t-arr[i],res,ans)
        res.pop()
    combinationSum2(arr,n,i+1,t,res,ans)
    
    return ans
    

candidates = [10,1,2,7,6,1,5]
target = 8

n = len(candidates)
combinationSum2(sorted(candidates),n,0,target,[],[])