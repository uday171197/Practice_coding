def soretdduplicate(nums):
    if len(nums)==1:
        return 1
    c= []
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            pass
        else:
            c.append(nums[i])
    if nums[len(nums)-2] != nums[len(nums)-1]:
        c.append(nums[len(nums)-1])
    return len(c)
            
nums = [0,0,1,1,1,2,2,3,3,4]
soretdduplicate(nums)


