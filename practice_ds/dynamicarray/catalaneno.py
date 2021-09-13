def catalanno(n,s,dp={}):
    # print(n,s,dp)
    if n==1 or n==0:
        return 1
    if s==1:
        dp[0]=1
        dp[1]=1
        return catalanno(n,s+1)
    elif s < n:
        cval = 0
        for i in range(s):
            cval +=dp[i]*dp[s-1-i]
        dp[s]=cval
        return catalanno(n,s+1)
    else:
        return list(dp.values())
    

catalanno(6,1)
