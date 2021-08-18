def function1(*arg):
    print(arg)
    
function1(1,2,3,4,5,6,7,8)

def function2(a,b,*arg):
    print(a,b,arg)
    
function2(1,2,3,4,5,6,7,8)



def function2(a,b,*c,d):
    print(a,b,c,d)
    
function2(1,2,3,4,5,6,7,8)