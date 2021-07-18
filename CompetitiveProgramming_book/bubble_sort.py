a = [2,3,1,4,6,5,7,8,9,12,3]
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]