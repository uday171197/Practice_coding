def minsum(m,n,arr,minvalue):
    print(minvalue)
    if m==0 and n ==0:
        return minvalue + arr[0][0]
    if m <0 or n < 0:
        return 100000
    lf = 1000000
    rf = 1000000
    if m-1 >-1:
        lf = minsum(m-1,n,arr,minvalue+arr[m][n])
    if n-1 > -1:
        rf = minsum(m,n-1,arr,minvalue+arr[m][n])
    return min(lf,rf)


arr = [[5,9,6],[11,5,2]]

m = len(arr)
n = len(arr[0])
minsum(m-1,n-1,arr,0)

def minsum(m,n,arr,minvalue,dp):
    print(minvalue,dp)
    if m==0 and n ==0:
        return minvalue + arr[0][0]
    if m <0 or n < 0:
        return None
    if dp[m][n] !=0:
        return dp[m][n]
    lf = None
    rf = None
    if m-1 >-1:
        lf = minsum(m-1,n,arr,minvalue+arr[m][n],dp)
    if n-1 > -1:
        rf = minsum(m,n-1,arr,minvalue+arr[m][n],dp)
    if not lf:
        dp[m][n] = rf
        return rf
    elif not rf:
        dp[m][n] = lf
        return lf
    dp[m][n] = min(lf,rf)
    return min(lf,rf)


dp = [[0,0,0],[0,0,0]]

minsum(m-1,n-1,arr,0,dp)


dp = [[0,0,0],[0,0,0]]
for i in range(m):
    for j in range(n):
        if i ==0 and j == 0:
            dp[i][j] = arr[i][j]
        else:
            lf = arr[i][j]+dp[i-1][j] if i-1 >-1 else None
            rf = arr[i][j]+dp[i][j-1] if j-1 >-1 else None
            if not lf:
                dp[i][j] = rf
            elif not rf:
                dp[i][j] = lf
            else:
                dp[i][j] = min(lf,rf)


prev = [0]*n
for i in range(m):
    temp = [0]*n
    for j in range(n):
        if i ==0 and j == 0:
            temp[j] = arr[i][j]
        else:
            lf = arr[i][j]+prev[j] if i-1 >-1 else None
            rf = arr[i][j]+temp[j-1] if j-1 >-1 else None
            print(lf,rf)
            if not lf:
                temp[j] = rf
            elif not rf:
                temp[j] = lf
            else:
                
                temp[j] = min(lf,rf)
    print(temp)
    prev = temp
prev[-1]








