def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        larr = arr[:mid]
        rarr = arr[mid:]
        mergesort(larr)
        mergesort(rarr)
        i=j=k=0
        while i<len(larr) and j<len(rarr):
            
            if larr[i]<=rarr[j]:
                arr[k]= larr[i]
                i+=1
            else:
                arr[k]= rarr[j]
                j+=1
            k+=1
                
        while i<len(larr):
            arr[k] = larr[i]
            i+=1
            k+=1
        while j<len(rarr):
            arr[k]= rarr[j]
            j+=1
            k+=1
            
arr = [6,4,3,7,2,9,1,8]
mergesort(arr)
print(arr)
    
    
    
# 1 example
# finding the duplicate element from an  array

a = [1,2,3,5,4,7,6,8,9,1,2]

mergesort(a)

for i in range(len(a)-1):
    if a[i]==a[i+1]:
        print('the duplicate element is {}'.format(a[i]))
        break


