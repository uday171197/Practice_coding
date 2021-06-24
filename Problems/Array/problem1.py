'''
    Reverse the array
'''

val = input('enter a vlaue : --->')
#method1

reverse = reversed(val)
print(f'method1: {reverse}')

# method 2

reverse = val[::-1]
print(f'method2: {reverse}')

# method3
reverse=''
for v in range(len(val)):
    reverse+=val[len(val)-1-v]
print(f'method3: {reverse}')
