
#  this function user the chacke variable that store the factorial that value is calculated . 
# we do not required to calculate again and again, we will use straignt farwrd
def factorial(n,chahe={}):
    if n==0:
        return 1
    elif n in chahe:
        return chahe[n] *factorial(n-1)
    else:
        print(f'factorial of {n}!')
        chahe[n]=n
        return n* factorial(n-1)

factorial(8)   