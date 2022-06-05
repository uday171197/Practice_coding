arr = [[1], [2,3], [3,6,7], [8,9,6,1]]
n = len(arr)

def allpath(i,j,n,arr,minv):
    if i == n:
        return minv
    
    lf = allpath(i+1,j,n,arr,minv+arr[i][j])
    rf = allpath(i+1,j+1,n,arr,minv+arr[i][j])
    return min(rf,lf)


allpath(0,0,n,arr,0)

def allpath(i,j,n,arr):
    if i == n:
        return arr[i][j]
    
    lf = arr[i][j] + allpath(i+1,j,n,arr)
    rf = arr[i][j] + allpath(i+1,j+1,n,arr)
    return min(rf,lf)

allpath(0,0,n-1,arr)


def allpathDP(i,j,n,arr,minv,dp):
    if i == n:
        return minv
    if dp[i][j] != -1:
        return dp[i][j] 
    lf = allpathDP(i+1,j,n,arr,minv+arr[i][j],dp)
    rf = allpathDP(i+1,j+1,n,arr,minv+arr[i][j],dp)
    dp[i][j] = min(rf,lf)
    return min(rf,lf)

dp = [[-1]*(i+1) for i in range(n)]


allpathDP(0,0,n,arr,0,dp)


#tabulation

dp = [[0]*(i+1) for i in range(n)]

for i in range(n):
    dp[n-1][i] = arr[n-1][i]


for i in range(n-2,-1,-1):
    for j in range(i,-1,-1):
        df = arr[i][j]+ dp[i+1][j]
        rf = arr[i][j]+ dp[i+1][j+1]
        dp[i][j] = min(df,rf)
dp[0][0]


# space optimization

arr = [[1], [2,3], [3,6,7], [8,9,6,1]]

previous = []
for i in range(n):
    previous.append(arr[n-1][i])
print(previous)
for i in range(n-2,-1,-1):
    temp = []
    for j in range(i,-1,-1):
        df = arr[i][j]+ previous[j]
        rf = arr[i][j]+ previous[j+1]
        temp.insert(0,min(df,rf))
    print(temp)
    previous = temp
previous[0]
    
[[12], [13, 11], [11, 12, 8], [8, 9, 6, 1]]


dp[0][0] 



