def frogjump(arr,n,i,dp,ans):
    if i >=n-1:
        return ans
    if dp.get(i):
        return dp[i]
        
    lf = frogjump(arr,n,i+1,dp,ans+abs(arr[i+1] - arr[i]))
    if i+2 < n: 
        rt = frogjump(arr,n,i+2,dp,ans+abs(arr[i+2] - arr[i]))
        dp[i] = min(lf,rt)
        return dp[i]
    dp[i] = min(lf,10000000)
    return dp[i]




arr = [30,10,60,10,60,50]
frogjump(arr,len(arr),0,{},0)


def frogjump(arr,n):
    if n == 0:
        return 0
    
    left = frogjump(arr,n-1) + abs(arr[n] - arr[n-1])
    right = 10000
    if n > 1:
        right = frogjump(arr,n-2) + abs(arr[n] - arr[n-2])
    return min(left,right)

arr = [30,10,60,10,60,50]
frogjump(arr,len(arr)-1)


def frogjump(arr,n,dp):
    print(dp)
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    left = frogjump(arr,n-1,dp) + abs(arr[n] - arr[n-1])
    right = 10000
    if n > 1:
        right = frogjump(arr,n-2,dp) + abs(arr[n] - arr[n-2])
    dp[n] = min(left,10000)
    return min(left,10000)

arr = [30,10,60,10,60,50]
frogjump(arr,len(arr)-1,[-1]*(len(arr)+1))


# tabulation 

dp = [-1] * len(arr)+1
dp[0] = 0
for i in range(2,len(arr)):
    
    left = dp[i-1]+abs(arr[i] - arr[i-1])
    right = 100000
    if i > 1:
        right = dp[i-2] + abs(arr[i] - arr[i-2])
    dp[i] = min(left,right)
dp[len(arr)-1]

# optimization


previous = 0
previous2 = 0
for i in range(2,len(arr)):
    
    left = previous+abs(arr[i] - arr[i-1])
    right = 100000
    if i > 1:
        right = previous2 + abs(arr[i] - arr[i-2])
    curr = min(left,right)
    previous2 = previous
    previous = curr


print(previous)

# write solution if he can able to take 1,2,3,4,5,6,...k steps


# 1 recursion
arr = [30,10,60,10,60,50]
n = len(arr)
k = 3
dp = [-1]*(n+1)
dp[0] = 0

for i in range(1,n):
    minvalue = 100000
    for j in range(1,k+1):
        if j <= i:
            jump = dp[i-j]+abs(arr[i]-arr[i-j])
            minvalue = min(minvalue,jump)
    dp[i] = minvalue
    
dp[n-1]
        


