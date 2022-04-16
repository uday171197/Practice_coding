
# using  parameterized method
def factorial(n,fact = 1):
    if n < 1:
        print(fact)
        return fact
    factorial(n-1,fact*n)

factorial(5)

# functional way

def factorial(n):
    if n ==0 :
        return 1
    return n * factorial(n-1)

factorial(3)