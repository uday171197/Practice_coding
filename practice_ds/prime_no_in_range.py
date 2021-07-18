def prime_no(n):
    a = {i for i in range(2,n+1)}
    print(a)
    for i in a:
        # i = list(a)[1]
        b = {i*j for j in range(i,round(n/i)+1)}
        print(i,b)
        a = a.difference(b)
        print(a)
    return sorted(a)
n =10
prime_no(10)
