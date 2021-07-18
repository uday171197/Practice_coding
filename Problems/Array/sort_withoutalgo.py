
a = [2,0,1]
b=[]
def compareval(a1,b1):
    if a1<b1:
        b.append(a1)
        b.append(b1)
    else:
        b.append(b1)
        b.append(a1)
        
if a[0]< a[1]:
    if a[0]<a[2]:
        b.append(a[0])
        compareval(a[1],a[2])
    else:
        b.append[a[2]]
        compareval(a[0],a[1])
elif a[1]<a[2]:
    b.append(a[1])
    compareval(a[0],a[2])
else:
    b.append(a[2])
    compareval(a[0],a[1])

print(b)


#method 2

def sortarray(arr):
    a,b,c=[],[],[]
    for i in arr:
        if i==0:
            a.append(i)
        elif i==1:
            b.append(i)
        elif i==2:
            c.append(i)
    a.extend(b)
    a.extend(c)
    return a 
arr = [0,2,1,2,0]
sortarray(arr)

# method 3
a,b,c = arr.count(0),arr.count(1),arr.count(2)
arr=[]
for i in range(a):
    arr.append(0)

for i in range(b):
    arr.append(1)

for i in range(c):
    arr.append(2)
    



