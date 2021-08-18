arr=[1, 4, 3, 2, 6, 7]

def minimumjump(arr,n):
    ind = 0
    count = 0
    while ind< n-1:
        if arr[ind]==0:
            count = count+1 if count else -1 
            break
        else:
             
            ind=arr.index(newind)
            count +=1
    return count

arr=[2,3,1,1,2,4,2,0,1,1]
minimumjump(arr,len(arr))


