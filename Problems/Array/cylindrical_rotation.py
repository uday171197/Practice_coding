def rotate_array(arr,n):
    for i in range(n):
        k=arr[-1]
        arr.pop()
        arr.insert(0,k)
    return arr
arr = [1,3]
rotate_array(arr,1)