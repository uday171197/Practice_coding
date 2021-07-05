d = 2
a = [1,2,3,4,6]
a = a[d:]+a[:d]

for i in range(d):
    a = a[1:]+a[:1]
    
a