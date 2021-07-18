def binary_search(arr,k):
    mid = len(arr)//2
    if k==arr[mid]:
        return 'found the value in array :{} ' .format(arr[mid])
    elif len(arr)==1:
        return 'dont have the value in array'
    elif k<arr[mid]:
        arr = arr[:mid]
        binary_search(arr,k)
    else:
        arr = arr[mid:]
        binary_search(arr,k)
    # for i in arr:
    #     if i==k:
    #         return 'found the value in array :{}' .format(k)
    # return 'dont have the value in array'
def binarysreatch(arr,k):
    a=0
    b = len(arr)
    while a<len(arr):
        mid = (a+b)//2
        if arr[mid]==k:
            print('found element')
            break
        elif len(arr[a:b])==1:
            print('found not found element')
            break
        elif k<arr[mid]:
            b= mid
        else:
            a = mid
    
arr= sorted([2,4,5,4,2,4,6,9])
k=2
binary_search(arr,k)
binarysreatch(arr,4)


    



        
