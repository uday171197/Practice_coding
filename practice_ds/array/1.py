def rotate(arr,r):
    a,b= [],[]
    for i in range(len(arr)):
        if i < r:
            a.append(arr[i])
        else:
            b.append(arr[i])
    return b+a

arr = [1,2,3,4,5,6]
rotate(arr,3)

