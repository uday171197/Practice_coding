
# 1 method
'''
TC = O(n**3)
SC = O(1)

'''
arr = [1,3,4,5,7,9]

n = len(arr)
def maxvalue(arr,n):
    maxv = 0
    for i in range(n):
        
        for j in range(i+2,n):
            val = arr[i]
            for k in range(0,n-j,2):
                # print(i,j,j+k)
                if j+k < n:
                    val += arr[j+k]
            # print('val-->',val)
            maxv = max(maxv,val)
    return maxv

maxvalue(arr,n)

# 2 method 
'''
TC = O(2**n)
SC = O(1)

'''
def fn(arr,n,dp):
    if n == 0:
        return arr[n]
    if n < 0:
        return 0
    if n in dp:
        return dp[n]
    value1 = arr[n]+fn(arr,n-2,dp)
    value2 = fn(arr,n-1,dp)
    dp[n] = max(value1,value2)
    return dp[n]

fn(arr,n-1,{})

# tabulation 

'''
TC = O(n)
SC = O(n)

'''
dp = {}
dp[0] = arr[0]
for i in range(1,n):
    take = arr[i]
    if i-2 >= 0:
        take+=dp[i-2]
    nottake = dp[i-1]
    print(take,nottake)
    dp[i] = max(take,nottake)
dp[n-1]


# tabulation  optimization

'''
TC = O(n)
SC = O()

'''
dp = {}
prevoius = arr[0]
previous2 = 0

for i in range(1,n):
    
    take = arr[i]
    if i-2 >= 0:
        take+=previous2
    nottake = prevoius
    curr = max(take,nottake)
    previous2 = prevoius
    prevoius = curr
prevoius


