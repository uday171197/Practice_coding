

# recursion

def climbing_stairs(n,dp):
    if n <= 1:
        return 1
    if dp.get(n):
        return dp[n]
    dp[n] = climbing_stairs(n-1,dp) + climbing_stairs(n-2,dp)
    return dp[n]

climbing_stairs(3,{})


# tabulat
n = 3
dp = {}
ans = 0
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

    