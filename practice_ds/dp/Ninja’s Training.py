

arr = [[1,2,5], [3 ,1 ,1],[3,3,3]]
# arr = [[10,40,70], [20 ,50 ,80],[30,60,90]]
n = len(arr)

# recursion

def trainingMaxPoint(arr,days,last):
    if days == 0:
        for task in range(3):
            maxv = 0
            if last != task:
                maxv = max(maxv,arr[days][task])
        return maxv
    maxvalue = 0
    for task in range(3):
        if task != last:
            point = arr[days][task] + trainingMaxPoint(arr,days-1,task)
            maxvalue = max(maxvalue,point)
            
            
    return maxvalue

#  dp
def trainingMaxPointDP(arr,days,last,dp):
    if days == 0:
        for task in range(3):
            maxv = 0
            if last != task:
                maxv = max(maxv,arr[days][task])
        return maxv
    
    if dp[days][last] != -1:
        return dp[days][last]
    
    maxvalue = 0
    for task in range(3):
        if task != last:
            point = arr[days][task] + trainingMaxPoint(arr,days-1,task)
            maxvalue = max(maxvalue,point)
            dp[days][last] = maxvalue
    
    return maxvalue
                

# arr = [[10,40,70], [20 ,50 ,80],[30,60,90]]
n = len(arr)
    
dp = [[-1,-1,-1,-1]]*(n)
trainingMaxPointDP(arr,n-1,3,dp)
print(dp)

# tabulation
def maxvaluef(days,last):
    maxv = 0
    for task in range(3):
        if last != task:
            
            maxv = max(maxv,arr[days][task])
            # print(task,last,arr[days][task],maxv)
    # print(maxv)
    return maxv
import copy
dp = copy.deepcopy([[-1,-1,-1,-1]]*(n))
for task in range(4):
    dp[0][task] = maxvaluef(0,task)

for days in range(1,n):
    for last in range(4):
        for task in range(3):
            if last != task:
                pt = arr[days][task] + dp[days-1][task]
                dp[days][last] = max(dp[days][last],pt)
dp