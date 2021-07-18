def subarraysum(a):
    mx = -100000
    sm =0
    for i in a:
        sm +=i
        if mx>sm:
            mx = sm
        if sm<0:
            sm = 0
    return sm

def submaxarray(arr):
    mx = -10000
    sm = 0
    for i in arr:
        sm = max(sm+i,i)
        mx = max(sm,mx)
    return mx
        
a = [-2,3,4,5,-10,3,4,5]         
subarraysum(a)

submaxarray(a)