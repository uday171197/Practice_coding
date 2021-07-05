

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
    
def hourglassSum(arr):
    hourarray = []
    maxval = 0
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            print(arr[i][j:j+3],arr[i+1][j:j+3],arr[i+2][j:j+3])
            sumarr = sum(arr[i][j:j+3])+arr[i+1][j:j+3][1]+sum(arr[i+2][j:j+3])
            print(sumarr)
            if maxval < sumarr:
                hourarray = [arr[i][j:j+3],arr[i+1][j:j+3],arr[i+2][j:j+3]]
                maxval = sumarr
    print(hourarray,maxval)
            
