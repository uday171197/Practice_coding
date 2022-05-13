# first we are going to develop febonacci using resursion
'''
TC =  O(2**n)
SC = O(n)
'''


def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
fibo(10)

#  we are going to create fibonacy using dynamic programming memorization
'''
TC = O(n)
SC = O(n)+O(n) (stackspace  + array)
'''
def fibo(n,dp):
    if n <=1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(n-1,dp)+fibo(n-2,dp)
    return dp[n]
n = 10
dp = [-1]*(n+1)
fibo(n,dp)

# tabulation
'''
TC = O(n)

SC = O(n) -- for Array 
'''
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])

# we can also able to imporve this also, because we required only previous 2 dala to calculate next one
# so we are going to store only those two value

'''
TC = O(n)

SC = O(n) -- for Array 
'''
a = 0
b = 1
for i in range(2,n+1):
    c = a+b
    a,b = b,c
print(c)

    