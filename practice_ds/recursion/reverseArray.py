
def reverseArray(arr,i):
    length = len(arr)
    if i >= length-1-i:
        return 
    arr[length-1-i],arr[i] = arr[i],arr[length-1-i]
    reverseArray(arr,i+1)
    
arr = list(range(100))
reverseArray(arr,0)

