nums = [0,3,7,2,5,8,4,6,0,1]

nums = set(nums)
maxcount = 0

for i in nums:
    count =0
    if i-1 not in nums and i+1 not in nums:
        maxcount = max(maxcount,1)
    elif i-1 not in nums and i+1 in nums:
        j = i
        while j in nums:
            count +=1
            j+=1
        maxcount = max(maxcount,count)

print(maxcount)
