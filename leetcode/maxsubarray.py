
def maxsubarray(nums):
    if len(nums)==1:
        return nums[0]
    else:
        maxvalue = -1000
        subarray = []
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                sumvalues= sum(nums[i:j])
                maxvalue =  sumvalues  if maxvalue < sumvalues else maxvalue
        return maxvalue













                 

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
nums = [5,4,-1,7,8]
maxsubarray(nums)



