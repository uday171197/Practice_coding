
def representbase(n,b):
    
    if b<2:
        raise ValueError('The base should be base >2')
    if n==0:
        return [0]
    r = []
    while n!=0:
        m = n%b
        r.insert(0,m)
        n=n//b
    # r = ' '.join(r)
    return r

representbase(3354,12)

def representbasemap(n,b,map1):
    
    if b<2:
        raise ValueError('The base should be base >2')
    if n==0:
        return [0]
    r = []
    sign = -1 if n<0 else 1
    while n!=0:
        m = n%b
        r.insert(0,m)
        n=n//b
    # r = ' '.join(r)
    r1 = [map1[i] for i in r]
    r2 = ''.join(r1)
    if n<0:
        r2 = '-1'+r2
    return r2
        
representbasemap(-3354,12,'01234567890abcdefghijklmnopqrstuvwxyz')
        
        
        
from random import randint
        