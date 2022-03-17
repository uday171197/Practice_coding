def InsertionSort(nums):
    for i in range(len(nums)):
        for j in range(i,0,-1):
            # print(j)
            if nums[j-1] > nums[j]:
                nums[j-1],nums[j] = nums[j],nums[j-1]
            else:
                break
        # print(nums[:i+1])
    return nums
            
InsertionSort([-2,45,0,11,-9])