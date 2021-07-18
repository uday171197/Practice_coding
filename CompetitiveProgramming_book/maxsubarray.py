a = [-1,-2,-3,-4]
a = list({1,2,3,-2,5})

#method 2
# it have n**2 time complexity
submax= 0
for i in range(len(a)):
    sumsub = 0
    for j in  a[i:]:
        sumsub += j
        if sumsub>submax:
            submax =sumsub
            
maxsum ,sumarray = -99999,-99999
for i in a:
    x = max(i,sumarray+i)
    maxsum = max(maxsum,x)
            
            
            



