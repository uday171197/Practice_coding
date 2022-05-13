#first I will going to solve using recursion 

'''
TC =  O(2**n)
SC = O(n)
'''

def climbings(n,c):
    if n<=1:
        c+=1
        # print(c)
        return c
    
    for step in [1,2]:
        c =  climbings(n-step,c)
    return c
n = 5
climbings(n,0)

# dynamic problem

'''
TC = O(n)
SC = O(n)+O(n) (stackspace  + array)
'''

def climbings(n,dp):
    if n<=1:
        return 1
    if dp[n] != -1:
        return dp[n]
    left =  climbings(n-1,dp)
    right =  climbings(n-2,dp)
    return left+right

n = 5
dp = [-1]*(n+1)
climbings(n,dp)

    