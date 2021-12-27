
numRows = 4

pascle = [[1]]
for i in range(2,numRows+1):
    row = []
    for j in range(i):
        if j ==0 or j == i-1:
            val = 1
        else:
            val = pascle[-1][j-1]+pascle[-1][j]
        row.append(val)
    pascle.append(row)
print(pascle)