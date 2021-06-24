'''
Prime factorization is process to find which prime no are multiply togather to get original no.
if we user this method it give you a time complexity of O(sqrt(m)) otherwise O(m).
'''

def prime_factorization(m):
    
    d=2
    p,f=[],[]
    if m==1:
        p.append(2)
        f.append(1)
        return p,f
    while m>1 and d*d<=m:
        k=0
        while m%d==0:
            m=m/d
            k+=1
        if k>0:
            print(d,k)
            p.append(d)
            f.append(k)
        d+=1
    if(m>1):
        p.append(m)
        f.append(1)
    return p,f
    
    
prime_factorization(1)



