# write an recursion function to print name N time
def print_name(N,name,i):
    if i>N:
        return None
    print(name)
    print_name(N,name,i+1)
    
print_name(5,'Uday',1)

#  write an recursion function to print linear no to N

def printNumber(N,i):
    if i>N:
        return None
    print(i)
    printNumber(N,i+1)
printNumber(5,1)

#  write an recursion function to print linear N to 1

def printNumber(N):
    if N<1:
        return None
    print(N)
    printNumber(N-1)
printNumber(5)

#  write an recursion function to print linear 1 to N using backtracking

def printNumber(N):
    if N<1:
        return None
    printNumber(N-1)
    print(N)
printNumber(5)

#  write an recursion function to print linear N to 1 using backtracking

def printNumber(N,i):
    if i>N:
        return None
    printNumber(N,i+1)
    print(i)
printNumber(5,1)

