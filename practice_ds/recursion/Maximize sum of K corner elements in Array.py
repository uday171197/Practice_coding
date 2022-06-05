

arr = [8, 4, 4, 8, 12, 3, 2, 9]
K = 3

def findMax(arr,k,start,end,maxsum):
    if k == 0:
        return maxsum
    
    start_max_sum = maxsum+arr[start]
    end_max_sum = maxsum+arr[end]
    
    ans = max(findMax(arr,k-1,start+1,end,start_max_sum),findMax(arr,k-1,start,end-1,end_max_sum))
    return ans


findMax(arr,K,0,len(arr)-1,0)

