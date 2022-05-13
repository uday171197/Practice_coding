
'''
This is a solution using power set
'''
def sumsubset(arr,n,i,res):
    if i > N:
        return
    print(res,sum(res))
    for j in range(i,n):
        res.append(arr[j])
        sumsubset(arr,n,j+1,res)
        res.pop()
    return




def sumsubset(arr,n,i,res):
    if i >= n:
        print(res,sum(res))
        return
    res.append(arr[i])
    sumsubset(arr,n,i+1,res)
    res.pop()
    sumsubset(arr,n,i+1,res)
    



N = 3
arr = [1,2,3]
sumsubset(arr,N,0,[])