def twosum(arr,t):
    d = {}
    for i in range(len(arr)):
        if t-arr[i] in d:
            return i, d[t-arr[i]]
        d[arr[i]] = i
        
nums = [2,7,11,15]
target = 9

twosum(nums,target)

    