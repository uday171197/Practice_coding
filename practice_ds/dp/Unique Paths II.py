

# recuraion
def unique_path(m,n,arr):
    if n>-1 and m > -1 and arr[m][n] == -1:
        return 0
    elif n == 0 and m == 0 and arr[m][n] == -1:
        return 0
    elif n == 0 and m == 0 and arr[m][n] == 0:
        return 1
    elif n < 0 or m < 0:
        return 0
    
    lf = unique_path(m-1,n,arr)
    rf = unique_path(m,n-1,arr)
    return lf+rf

arr = [[0,0,0],[0,-1,0],[0,0,0]]
m = len(arr)
n = len(arr[0])
unique_path(m-1,n-1,arr)


# dp
def unique_path(m,n,arr,dp):
    if n>-1 and m > -1 and arr[m][n] == -1:
        return 0
    elif n == 0 and m == 0 and arr[m][n] == -1:
        return 0
    elif n == 0 and m == 0 and arr[m][n] == 0:
        return 1
    elif n < 0 or m < 0:
        return 0
    if dp[m][n] != 0:
        return dp[m][n]
    
    lf = unique_path(m-1,n,arr,dp)
    rf = unique_path(m,n-1,arr,dp)
    dp[m][n] = lf+rf
    
    return lf+rf


dp = [[0]*n]*m
unique_path(m-1,n-1,arr,dp)

# tabulation
import copy
dp = copy.deepcopy([[0]*n]*m)

for i in range(m):
    for j in range(n):
        if i ==0 and j ==0 and arr[i][j] == 0:
            dp[i][j] = 1
        else:
            lf = dp[i-1][j] if i > -1 and arr[i][j] != -1 else 0
            rf = dp[i][j-1] if j > -1 and arr[i][j] != -1 else 0
            dp[i][j] = lf+rf
        print(dp)


dp[m-1][n-1]
