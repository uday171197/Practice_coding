
def total_possible_tiling(n,start,dp={}):
    print(dp)
    if start == 1:
        dp[start]=1
        return total_possible_tiling(n,start+1)
    elif start == 2:
        dp[start]=2
        return total_possible_tiling(n,start+1)
    elif start <= n:
        dp[start]=dp[start-1]+dp[start-2]
        return total_possible_tiling(n,start+1)
    else:
        return dp[start-1]

total_possible_tiling(5,1)
        
        
        
    