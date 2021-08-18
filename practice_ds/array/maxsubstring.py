arr = [1,2,-3,4,-5,9]

def findsubmax(arr):
    maxsum,sumsub = 0,0
    for i in arr:
        sumsub += i
        sumsub = 0 if sumsub < 0 else sumsub
        maxsum = sumsub if sumsub > maxsum else maxsum
    return maxsum

findsubmax(arr)