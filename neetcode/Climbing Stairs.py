# recursion

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n ==0:
        return 1
    
    lf = climbStairs(n-1)
    rf = 0
    if n >1:
        rf = climbStairs(n-2)
        
    return rf+lf
n = 3
climbStairs(n)


# memorization


def climbStairs(n,dp):
    """
    :type n: int
    :rtype: int
    """
    if n ==0:
        return 1
    if dp[n] != -1:
        return dp[n]
    lf = climbStairs(n-1,dp)
    rf = 0
    if n >1:
        rf = climbStairs(n-2,dp)
    dp[n] = rf+lf
    return dp[n]
n = 3
dp = [-1]*(n+1)
climbStairs(n,dp)


# tabulation
n = 3
dp = [-1]*(n+1)

dp[0] = 1
for i in range(1,n+1):
    dp[i] = dp[i-1]
    if i>1:
        dp[i] +=dp[i-2]
    print(dp[i])

print(dp[n])


# Space optimization


n = 3

previous = 1
previous2 = 0
for i in range(1,n+1):
    curr = previous
    if i>1:
        curr +=previous2
    print(previous,previous2,curr)
    previous2 = previous
    previous = curr
    

print(previous)
