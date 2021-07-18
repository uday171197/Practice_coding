'''
Find the maximum and minimum element in an array
'''

arr = list(map(lambda x:int(x) , input().split()))

# method 1
maxval = max(arr)
minval = min(arr)
print(maxval,minval)

# method 2
sortedArr = sorted(arr)
print(sortedArr[-1],sortedArr[0])

#method 3
maxval,minval = 0,99999999999
for i in arr:
    if maxval < i:
        maxval = i
    elif minval>i:
        minval = i
print(maxval,minval)



