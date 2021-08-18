
def mergesort(arr):
    if len(arr)>1:
        m = len(arr)//2
        arr1 = arr[:m]
        arr2 = arr[m:]
        mergesort(arr1)
        mergesort(arr2)
        i=k=j=0
        while i<len(arr1) and j < len(arr2):
            if arr1[i]<arr2[j]:
                arr[k] = arr1[i]
                i+=1
            else:
                arr[k] = arr2[j]
                j+=1
            k+=1
        while i<len(arr1):
            arr[k]= arr1[i]
            i+=1
            k+=1
        while j < len(arr2):
            arr[k]=arr2[j]
            j+=1
            k+=1

def twosum(arr,t):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == t:
                return [i,j]
            elif arr[i]+arr[j] > t:
                break
           
           
def twosum2(nums,target):
    dictval = {}
    for i,j in enumerate(nums):
        r = target-j
        if r in dictval:
            return [dictval[r],i]
        else:
            dictval[j]=i
        
        


arr = [3,2,4]
t = 6
twosum2(arr,t)  

 



        
        

