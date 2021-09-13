

# first I will going to make a closer that will calculte the average of value that we have passed

def averager():
    total = 0
    count = 0
    def add(num):
        nonlocal total
        nonlocal count
        total += num
        count += 1
        return total/count
    return add


a = averager()

a(60)

# create a counter  thet will get the time after 
from time import perf_counter
def timer():
    start = perf_counter()
    def times():
        nonlocal start
        return perf_counter() - start
    return times
t1 = timer()
t1()


def counter(init_count=0):
    def inc(increamenter=1):
        nonlocal init_count
        init_count += increamenter
        return init_count
    return inc
inc = counter()
inc(4)


        

    
    