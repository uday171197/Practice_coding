
# using kadane's algoritham to calculate mxa product of subarray

def maxproduct(nums):
    ans = nums[0]
    maxvalue = 1
    minvalue = 1
    for i in nums:
        maxvalue ,minvalue= max(i,i*maxvalue,i*minvalue),min(i,i*maxvalue,i*minvalue)
        # print(maxvalue,minvalue)
        ans = max(ans,maxvalue)
        # print(ans)
    return ans

nums = [-3,-14,-3]
maxproduct(nums)

-2*-2
