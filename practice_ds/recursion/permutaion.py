def permutaion(arr,res,d):
    # print("----------->",res)
    if len(arr) == len(res):
        print(res)
        return
        
    for i in range(1,len(arr)+1):
        if not d.get(i):
            res.append(i)
            d[i] = True
            permutaion(arr,res,d)
            res.pop()
            d[i] = False
    return
        
arr = [1,2,3]
# arr.remove(1)
permutaion(arr,[],{})


# swapping method 

def swapping(arr,n,ind):
    if ind == n:
        print(arr)
        return
        
    for i in range(ind,n):
        print(ind,i)
        arr[ind],arr[i] = arr[i],arr[ind]
        swapping(arr,n,i+1)
        arr[ind],arr[i] = arr[i],arr[ind]

arr = [1,2,3]
swapping(arr,len(arr),0)

