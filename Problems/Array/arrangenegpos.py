def arrangeno(arr):
    a,b = [],[]
    for n in arr:
        if n < 0:
            a.append(n)
        else:
            b.append(n)
    for i in range(len(a)):
        arr[i] = a[i]
        
    for j in range(len(a),(len(b)+len(a))):
        print(j)
        arr[j] = b[j-len(a)]
    return arr
arr = [-2,-4,3,-10,4,5,-6]       
arrangeno(arr)

# method 2

def arrangeno(arr):
    j=0
    for i,n in enumerate(arr):
        if n < 0:
            (arr[j],arr[i]) = (n,arr[j])
            j+=1
    return arr

arrangeno(arr)
    
