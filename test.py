
s = "0a"
r = ''
i = 'a'
for i in s:
    if (ord('z') >= ord(i.lower()) and ord(i.lower()) >=  ord('a')) or (ord('0') <= ord(i.lower()) and ord(i.lower()) <=  ord('9')):
        r+=i.lower()
n = len(r)
for i in range(n//2):
    print(r[i], r[n-i-1])
    if r[i] != r[n-i-1]:
        print('YES')
        



        
        