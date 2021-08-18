a = lambda x : x**2
a(10)

# how to use key in  sorted function ,
l = [1,4,2,3,6,9,7,8,7,6,4,]
sorted(l)

l = ['c','D','a','E','F']
sorted(l)

# ['D', 'E', 'F', 'a', 'c'] this is not the sorted value  we will use the kay argument which contain the f function 
# that will convert the value  in upper case and  sort the value based on that upercase value 
x = 'k'

sorted(l,key=lambda x:x.upper())


# 
mark = {'a':10,'z':100,'c':50,'m':89,'r':35}
sorted(mark,key = lambda x:mark[x])
    