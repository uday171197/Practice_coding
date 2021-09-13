def counter(fn):
    count=0
    def inner(*arg,**krgs):
        print('hii')
        nonlocal count
        count+=1
        print(f'{fn.__name__}--------{count}')
        return fn(*arg,**krgs)
    return inner

def add(a,b):
    return a+b

add = counter(add)
add(1,2)




@counter
def multi(a,b):
    return a* b


multi = counter(multi)
multi(2,6)



# application 1
def timer(fn):
    from time import perf_counter
    def inner(*arg,**kwrg):
        start = perf_counter()
        result = fn(*arg,**kwrg)
        end = perf_counter()
        diff = end-start
        print('execution time fro function {}  is : {}s'.format(fn.__name__,diff))
        return result
    return inner

@timer
def add():
    return 3+6


add()

a = [2,3,4,5,6,7]
a [-3:]