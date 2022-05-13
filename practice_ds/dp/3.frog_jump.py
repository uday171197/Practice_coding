
# first I will going to solve using recursion 

def frogJump(arr,n,i,energy,res):
    if i >= n-1:
        # print(energy)
        res.append(energy)
        return energy
    en = abs(arr[i+1]-arr[i])
    left = frogJump(arr,n,i+1,energy+en,res)
    if i <2:
        en = abs(arr[i+2]-arr[i])
        # print(en)
        right = frogJump(arr,n,i+2,energy+en,res)
        
        return min(left,right)
    return left

arr = [10,20,30,10]
frogJump(arr,len(arr),0,0,[])


def frogJump(arr,n):
    if n == 0:
        return 0
    
    left = frogJump(arr,n-1)+abs(arr[n-1]-arr[n])
    if n >1:
        right = frogJump(arr,n-2)+abs(arr[n-2]-arr[n])
        return min(left,right)
    return min(left,10000000)

arr = [30,10,60,10,60,50]
frogJump(arr,len(arr)-1)
    

    