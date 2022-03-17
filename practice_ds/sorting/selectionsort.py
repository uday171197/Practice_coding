def selectionSort(nums):
    for i in range(len(nums)):
        minindex = i
        for j in range(i,len(nums)):
            if nums[minindex] > nums[j]:
                minindex = j
        nums[i],nums[minindex] = nums[minindex],nums[i]
    return nums
            
selectionSort([-2,45,0,11,-9])