'''
here we are going to code for prome no.
'''

def prime(n):
    prime = True
    for i in range(2,n):
        if n%i==0:
            prime = False
    if prime:
        print('No. is prime ')
    else:
        print('not a priem No.')


