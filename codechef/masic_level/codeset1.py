# proble1

a,b,x,y = list(map(lambda x:int(x),input().split()))
print(a*x + b*y)

# problem2
x = 110
x = int(input())
if x%5==0 and x%11==0:
    print('BOTH')
elif x%5==0 or x%11==0:
    print('ONE')
else:
    print('NONE')

#problem 3
n = int(input())
a = list(map(lambda x:i if n%i==0 else '',range(1,n+1)))
n=11
int(97**0.5)
import math 
s,p = [],[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        if n//i==i:
            s.append(str(i))
        else:
            s.append(str(i))
            p.append(str(int(n/i)))
c = s+p[::-1]
print(' '.join(c),end=' ')