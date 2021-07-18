# method1
def kthmaxmin(a,k):
    sorteda =sorted(a)
    kthmin = sorteda[k-1]
    kthmax = sorteda[-k]
    print(sorteda)
    return kthmin,kthmax

a = [1,3,5,7,2,8,9,45,33,45,66,2,34]
kthmaxmin(a,5)

# method2
# it have nlogn time complexity
def mergesort(arr):
    if len(arr)>1:
        m= len(arr)//2
        left = arr[:m]
        right = arr[m:]
        
        mergesort(left)
        mergesort(right)
        i,j,k=0
        
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                j+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i,k=i+1,k+1
        while j<len(right):
            arr[k]=left[j]
            j,k=j+1,k+1
                            
def kthmaxminvalue(a,k):
    mergesort(a)
    print(a)
    kthmax= a[-k]
    kthmin = a[k-1]
    print(kthmin,kthmax)
    
    
kthmaxminvalue([1,3,5,7,2,8,9,45,33,45,66,2,34],3)
        

