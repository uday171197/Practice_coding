
#  this is the fibonacci suing multiple recursion call
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    

fibo(4)  # 3


