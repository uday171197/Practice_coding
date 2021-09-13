def maxsumnonconsucative(arr):
    dp={}
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        dp[i]  = max(dp[i-1],arr[i]+dp[i-2])
    return dp[i]
    
arr = [1,2,3,4,5,6,7]
maxsumnonconsucative(arr)

def maxnonconsum(arr,start,dp={}):
    # print(dp)
    if start ==0:
        dp[start]=arr[start]
        return maxnonconsum(arr,start+1,dp)
    elif start ==1:
        dp[start]=max(arr[start],arr[start-1])
        return maxnonconsum(arr,start+1,dp)
    elif start < len(arr):
        dp[start] = max(dp[start-1],arr[start]+dp[start-2])
        return maxnonconsum(arr,start+1,dp)
    else:
        return dp[start-1]
    
maxnonconsum(arr,0)
    