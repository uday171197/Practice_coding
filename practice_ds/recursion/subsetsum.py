# using power set  
'''
it have time complexity of O(2**n)*n 
'''
def subsetSum1(arr,ind,res,sumvalue,ans):
    if ind >= len(arr):
        return
    # print(res)
    print(sumvalue)
    ans.append(sumvalue)
    for i in range(ind+1,len(arr)):
        res.append(arr[i])
        subsetSum1(arr,i,res,sumvalue+arr[i],ans)
        res.pop()
    return ans

arr = [3,2,1]
sorted(subsetSum1(arr,-1,[],0,[]))

'''
we have optimized the solution to O(2**n) + 2**n(log(2**n))
'''
from copy import deepcopy
def subsetSum(arr,ind,res,ans):
    if ind >= len(arr):
        ans.append(sum(res))
        # print(ans)
        return ans
    # print(ind)
    res.append(arr[ind])
    ans = subsetSum(arr,ind+1,res,ans)
    res.pop()
    ans = subsetSum(arr,ind+1,res,ans)
    return ans

arr = [3,1,4]
sorted(subsetSum(arr,0,[],[]))


