
nums = [1,2,3,4]

prefix = []
mult = 1
for i in nums:
    mult *= i
    prefix.append(mult)
    
    
postfix = []
mult = 1
for i in nums[::-1]:
    mult *= i
    postfix.append(mult)

postfix = postfix[::-1]
res = []
for i in range(len(nums)):
    if i == 0:
        res.append(postfix[i+1])
    elif i == len(nums)-1:
        res.append(prefix[i-1])
    else:
        res.append(prefix[i-1] * postfix[i+1])
        
        
        
reslt = [1]*len(nums)
mult = 1
for i in range(len(nums)-1,0,-1):
    if i-1 >=0:
        mult *= nums[i]
        reslt[i-1] = reslt[i-1]*mult
    
mult = 1
for i in range(len(nums)):
    if i+1 < len(nums):
        mult *= nums[i]
        reslt[i+1] = reslt[i+1]*mult


        
        
        
        
