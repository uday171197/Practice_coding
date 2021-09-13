# o(n**3)


def sum3(nums):
    res = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if i!=j and j!=k and k!=i  and  sum([nums[i],nums[j],nums[k]]) ==0:
                        res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                    
    return res

nums = [-1,0,1,2,-1,-4]
ands = sum3(nums)
ans = [[-1, 0, 1], [-1, 2, -1]]
[0, 1, -1]  in ans



def sumthree(nums):
    res = set()
    for i in range(len(nums)):
        store = {}
        for j in range(len(nums)):
            if -(nums[i]+nums[j]) in store:
                k = store[-(nums[i]+nums[j])]
                if i!=j and j!=k and i!=k:
                    res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
            else:
                store[nums[j]] = j
    return [list(i) for i in res]
    
nums = [-1,0,1,2,-1,-4]
ands = sumthree(nums)





