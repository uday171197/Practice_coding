
# using  parameterized method
def sumvalue(n,sumv = 0):
    if n < 1:
        print(sumv)
        return sumv
    sumvalue(n-1,sumv+n)

sumvalue(5,0)

# functional way

def nsum(n):
    if n ==0 :
        return 0
    return n + nsum(n-1)

nsum(3)


    