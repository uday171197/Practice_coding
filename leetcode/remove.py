from _typeshed import ReadableBuffer


def remove(nums,val):
    if len(nums)==1:
        return 1
    c= 0
    for i in range(len(nums)):
        if nums[i] == val:
            pass
        else:
            nums[c] = nums[i]
            c+=1
    for i in range(c,len(nums)):
        nums[c] = '_'
        c+=1
    return nums
            
nums = [0,1,2,2,3,0,4,2]
remove(nums,2)