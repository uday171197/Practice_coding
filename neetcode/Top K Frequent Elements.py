from email.mime import base


nums = [1,1,1,2,2,3]
k = 2

dic = {}
for i in nums:
    dic[i] +=1 + dic.get(i,0)

res = []

for j in range(k):
    maxv = 0
    keyvalue = 0
    for key,val in dic.items():
        if val > maxv:
            maxv = val
            keyvalue = key
    dic.pop(keyvalue)
    res.append(keyvalue)
    maxv = 0
    keyvalue = 0
    

