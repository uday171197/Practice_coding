def ContainerMostWater(arr):
    v=0
    i,j= 0,len(arr)-1
    while j>i:
        diffval = j-i
        newval = arr[i] if arr[i] < arr[j] else arr[j]
        newV = diffval* newval
        v = newV if newV > v else v
        if arr[i] <= arr[j]:
                i+=1
        else:
            j-=1
    return v

arr = [1,8,6,2,5,4,8,3,7]
arr = [1,2,3,4]
ContainerMostWater(arr)

