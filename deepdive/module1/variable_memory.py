# first I am going to decleare a variabe 
a = 5
#  The variable a basically store the reference of object i mamery , it doen't store directly value. 
# will find the memory address of that variable using id()
id(a)
# we cam convert that address into hexadecimal foprmat using hex()
hex(id(a))

'''Reference Count'''

# reference count is nothing but no of same reference object are store in memory.

import sys
sys.getrefcount(a)
b = a


# -------------------------------variable re-assignment--------------------------------- 
a = 2
hex(id(a)) #'0x955ce0'

a = 100
hex(id(a)) #'0x956920'

a = a+1 
hex(id(a))  # 0x956940

# you can see that the value have same memory address that have in initially . 
# that mean whenever we will going to assignanother value then it will store at different memory location
a = 2
hex(id(a)) #0x955ce0
b = 2 
hex(id(a)) #0x955ce0


#---------------------------------------------variable mutubility----------------------

a = [1,2,3]
hex(id(a)) #0x7f952cc44400

a.append(5)
hex(id(a)) #0x7f952cc44400

a = a + [6]
hex(id(a)) #0x7f952d57a340

# that means if we use  the list operations to change the value then it is immutable
# and if we add an another list then if is mutable means it memory address changed

a = ([1,2,3],[1,3])
hex(id(b)) #0x955ce0
a[0]

a[0].append(5)
hex(id(b)) #0x955ce0
a[0]

#  ----------------------------function argument & mutability----------------------------

# 1).the immutable element are safe from unintendedside effect

def process(s):
    print(f'befor #{id(s)}') #140285448050992
    s =s+'hello'
    print(f'after #{id(s)}') #140285448051120

var1 = 'hii'
print(f'#{id(var1)}') #140285448050992

process(var1)
print(f'#{id(var1)}') #140285448050992

# you can see that the reference address of var1 are remain same after calling the function ,
# the s variable are stored at different memory address

# 2).the mutable element are not safe from unintendedside effect
def process(s):
    print(f'befor #{id(s)}') #140285428253568
    s.append(100)
    print(f'after #{id(s)}') #140285428253568

var1 = [1,2,3]
print(f'#{id(var1)}') #140285428253568

process(var1)
print(f'#{var1}')
print(f'#{id(var1)}') #140285428253568

# you can see that the address of object are same after changing the internal state of object 

# 3. we are going to check effect on tuples

def process(s):
    print(f'befor #{id(s)}') #140285426604416
    s[0].append(100)
    print(f'after #{id(s)}') #140285426604416

var1 = ([1,2,3],'a')
print(f'#{id(var1)}') #140285426604416

process(var1)
print(f'#{var1}')
print(f'#{id(var1)}') #140285426604416


# you can see that the address of object are same after changing the internal state of object 

# --------------------------shared refencing and mutability---------------------------
a = 10
b = a
print(f'#{id(a)}') #9788896
print(f'#{id(b)}') #9788896


a = [1,2,3]
b = a
print(f'#{id(a)}') #140285428253568
print(f'#{id(b)}') #140285428253568

a.append(5)
print(f'#{id(a)}') #140285428253568

