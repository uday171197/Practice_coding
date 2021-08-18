
def reversearray(arr,start,end):
    startind,endind = start,end
    # startind,endind= 0,2
    while startind < (start+end)/2:
        arr[startind],arr[endind] = arr[endind],arr[startind]
        startind,endind = startind+1,endind-1
    


def reverse(arr,n,d):
    reversearray(arr,0,d-1)
    reversearray(arr,d,n)
    reversearray(arr,0,n)

arr = [1,2,3,4,5,6,7]
n,d = len(arr)-1,2
reverse(arr,6,2)