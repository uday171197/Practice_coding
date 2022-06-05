arr = [[1,2,10,400],
[100,3,2,1],
[1,1,20,2],
[1,2,2,1]]


# recursion
row = len(arr)
col = len(arr[0])
def findmaxsum(i,j,row,col,arr):
    print(i,j)
    if j > col-1:
        return 0
    if i == row-1:
        return arr[i][j]
    lf = 0
    if j-1 > -1:
        lf = arr[i][j] + findmaxsum(i+1,j-1,row,col,arr)
    rf = 0
    if j+1 <= col:
        rf = arr[i][j] + findmaxsum(i+1,j+1,row,col,arr)
    df = arr[i][j] + findmaxsum(i+1,j,row,col,arr)
    return max(lf,rf,df)
maxv = 0

for i in range(col):
    maxv = max(maxv,findmaxsum(0,i,row,col,arr))


# DP

def findmaxsumDP(i,j,row,col,arr,dp):
    if j>col-1:
        return 0
    if i == row-1:
        return arr[i][j]
    if dp[i][j] != -1:
        return dp[i][j]
    lf = 0
    if j-1 > -1:
        lf = arr[i][j] + findmaxsumDP(i+1,j-1,row,col,arr,dp)
    rf = 0
    if j+1 <= col:
        rf = arr[i][j] + findmaxsumDP(i+1,j+1,row,col,arr,dp)
    df = arr[i][j] + findmaxsumDP(i+1,j,row,col,arr,dp)
    dp[i][j] = max(lf,rf,df)
    return max(lf,rf,df)
    
dp = [[-1]*col for i in range(row)]
for i in range(col):
    maxv = max(maxv,findmaxsumDP(0,i,row,col,arr,dp))
print(maxv)

# tabulation
dp = [[-1]*col for i in range(row)]
for i in range(col):
    dp[0][i] = arr[0][i]

for i in range(1,col):
    for j in range(i,col):
        pass
        


API_KEY = "AIzaSyAYJSSMLNeKv_PI_AcKtuCamGaZuiWMLtI"
url = "https://translation.googleapis.com/language/translate/v2/?q={}&target={}&key={}".format('hello', 'hi',API_KEY)


import requests
data = requests.get(url, verify=False)
data = data.json()
print(data)



