from copy import deepcopy
# solution 1
def combinedsum2(candidates,ind,target,res,ans):
        if ind >= len(candidates):
            if target == 0 and res not in ans:
                print(res)
                ans.append(deepcopy(res))
            return ans
        if candidates[ind] <= target:
            res.append(candidates[ind])
            ans = combinedsum2(candidates,ind+1,target-candidates[ind],res,ans)
            res.pop()

        ans = combinedsum2(candidates,ind+1,target,res,ans)
        return ans

# optimized solution
'''
so the time complexity for this is O(2**n )*k , 
where k is the no of time we have chacked the combination
and space complexity is K*X

'''

def combinedsum2(candidates,ind,target,res,ans):
    if target == 0 and res not in ans:
        print(res)
        ans.append(deepcopy(res))
        return ans
    for indx in range(ind,len(candidates)):
        if indx > ind and candidates[indx] == candidates[indx-1]:
            continue
        if candidates[indx] > target:
            break
        res.append(candidates[indx])
        ans = combinedsum2(candidates,indx+1,target-candidates[indx],res,ans)
        res.pop()
       
    return ans

candidates = [10,1,2,7,6,1,5]
target = 8

combinedsum2(sorted(candidates),0,target,[],[])
