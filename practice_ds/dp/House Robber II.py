def maxmoney(arr):
    n = len(arr)
    previous = arr[0]
    
    previous2 =  0
    
    for i in range(1,n):
        keep = arr[i]
        if i-2 >= 0:
            keep += previous2
            
        notkeep = previous

        curr = max(keep,notkeep)
        previous2 = previous
        previous = curr
    return previous





arr = [6 ,5, 4, 3, 2, 1, 7]
n = len(arr)
if n == 1:
    print(arr[0])
else:
    print(max(maxmoney(arr[1:]),maxmoney(arr[:-1:])))

    