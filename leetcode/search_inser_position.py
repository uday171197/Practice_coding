
def searchInsertIndex(nums,target):
    mid = len(nums)//2
    if mid == 0:
        if target <= nums[mid]:
            return mid
        else:
            return mid+1
    if target < nums[mid]:
        for ind,value in enumerate(nums[:mid]):
            if value >= target:
                return ind 
    else:
        for ind,value in enumerate(nums[mid+1:]):
            if value >= target:
                return ind + mid
    return  len(nums)
            
        

nums = [1,3,5,6]
target = 2

searchInsertIndex([1],0)


1//2