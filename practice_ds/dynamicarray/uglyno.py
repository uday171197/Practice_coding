def develop(no,a):
    while no%a==0:
        no = no//a
    return no

def ugly(no):
    no = develop(no,2)
    no = develop(no,3)
    no = develop(no,5)
    return 1 if no==1 else 0

    
    


def uglynocount(n):
    i=count = 1
    while count < n:
        i+=1
        if ugly(i):
            count +=1
            # print(count)
        
        print(count,i)
    return i

uglynocount(15)

def dpugly(n,i2,i3,i5,s,dp):
    print(n,i2,i3,i5,s,dp)
    if s<=n:
        print(dp[i2]*2,dp[i3]*3,dp[i5]*5)
        dp[s] = min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
        if dp[s] == dp[i2]*2:
            i2+=1
        elif dp[s] == dp[i3]*3:
            i3+=1
        elif dp[s] == dp[i5]*5:
            i5+=1
        return dpugly(n,i2,i3,i5,s+1,dp)
    return dp[s-1]

dpugly(15,0,0,0,1,dp={0:1})