def lattershift(s,shifts):
    # a = [ for i in range(len(shifts))]
    # list(map(lambda i: sum(shifts[i:])%26,range(len(shifts))))
    from itertools import accumulate
    a = list(accumulate(shifts[::-1]))[::-1]
    print(a)
    r= ''
    for i in range(len(a)):
        r += chr(ord(s[i])+a[i]%26) if (ord(s[i])+a[i]%26) <= 122 else chr((ord(s[i])+a[i]%26)%122+96)
    return r




s = "ruu"
shifts = [26,9,17]
lattershift(s,shifts)
