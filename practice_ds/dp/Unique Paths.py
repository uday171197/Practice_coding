mt = [[1,2],[1,2]]
m = len(mt)
n = len(mt[0])

#recursion

def uniquePath(m,n):
    if m==0 and n==0:
        return 1
    if m<0 or n < 0:
        return 0
    lf = uniquePath(m-1,n)
    rt = uniquePath(m,n-1)
    return lf+rt


# memorization

def uniquePath(m,n,dp):
    if m==0 and n==0:
        return 1
    if m<0 or n < 0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    lf = uniquePath(m-1,n,dp)
    rt = uniquePath(m,n-1,dp)
    dp[m][n] = lf+rt
    return dp[m][n]

dp = [[-1]*m,[-1]*n]

uniquePath(m-1,n-1,dp)

# tabulation

dp = [[0]*m,[0]*n]

for i in range(m):
    for j in range(n):
        if i ==0 and j ==0:
            dp[i][j] = 1
        else:
            
            up = dp[i-1][j] if i > -1 else 0
            down  = dp[i][j-1] if j > -1 else 0
            print(up ,down)
            dp[i][j] = up + down
            
print(dp[m-1][n-1])

# space optimization

prev = [0]*n
for i in range(m):
    temp = [0]*n
    for j in range(n):
        if i ==0 and j ==0:
            temp[j] = 1
        else:
            temp[j] = prev[j] + temp[j-1]
    prev = temp
            
print(prev[n-1])
        
