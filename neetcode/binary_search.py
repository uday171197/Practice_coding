nums = [1,0,5]
target = 1

def binarySearch(nums,target,l,r):
    m = (l+r-1)//2
    if l>=r:
        return -1
    
    print(l,m,r,nums[m])
    if nums[m] == target:
        print('found value')
        return m
    elif target > nums[m]:
        out = binarySearch(nums,target,m+1,r)
    else:
        out = binarySearch(nums,target,l,m)
    return out
    
   
def binarySearch(nums,target):
    l,r = 0,len(nums)-1
    
    while l<=r:
        m =  l + ((r - l) // 2)
        if nums[m] == target:
            return m
        elif target > nums[m]:
            l = m+1
        else:
            r = m-1
    return -1 

binarySearch(nums,target)