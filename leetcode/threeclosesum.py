

def threesumcloser(nums,target):
    res = 1000000
    sums= []
    diff = -100000
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                sumval = sum([nums[i],nums[j],nums[k]])
                print(sumval)
                sums.append(target-sumval)
                # print(abs(sumval-target) , abs(res-target))
                if abs(sumval-target) > diff: 
                    diff = abs(sumval-target)
                    res = sumval
                elif sumval == target:
                    return sumval
                
                    
    return res,sums

[0,2,1,-3]
1

nums = [0,2,1,-3]
threesumcloser(nums,1)



def sum3(nums,target):
    nums = sorted(nums)
    sumval = 0
    difference = float('inf')
    length = len(nums)
    for i in range(length-2):
        s,e= i+1,length-1
        while s < e:
            sumv = nums[i]+nums[s]+nums[e]
            if sumv ==target:
                return target
            elif abs(sumv-target) < difference:
                difference = abs(sumv-target)
                sumval = sumv
            if sumv > target:
                e-=1
            else:
                s+=1
    return sumval


    
nums = [0,2,1,-3]
sum3(nums,1)

