from threading import Thread

def table(n):
    for i in range(100):
        if n:
            print('Eating')
        else:
            print('Running')
t = Thread(target=table,args=(0,))
t.start()
for i in range(100):
    print('Main Thread')
# t1 = Thread(target=table,args=(1,))
# t1.start()


