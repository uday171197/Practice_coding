arr = [1, 5, 15, 10]


def mindifference(arr,k):
    maxval,minval = 0,0
    n= len(arr)
    maxdiff = arr[n-1]-arr[0]
    
    smalltower =arr[0]+k
    maxtower = arr[n-1]-k
    
    # maxdiff = 0
    for i in range(1,len(arr)):
        minval = min(smalltower,arr[i]-k)
        maxval = max(maxtower,arr[i-1]+k)
        if minval<0:
            continue
        maxdiff = min(maxdiff,maxval-minval)
    return maxdiff

mindifference(sorted(arr),3)      

