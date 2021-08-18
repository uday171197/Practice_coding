n = 10
while 1:
    try:
        # if n == 1:
        b=n/n-1
        print(b)
            # break
        n=n-1
    except:
        print('exception occure')
        break
    finally:
        print('it will always run')
else:
    print('no exception occure')
    
