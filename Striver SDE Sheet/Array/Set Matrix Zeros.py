def setmetrix(matrix):
    col_index = []
    row_index = []
    n,m = len(matrix[0]),len(matrix)
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                col_index.append(i)
                row_index.append(j)
                
    if col_index:
        for i in range(len(col_index)):
            for _ in range(n):
                matrix[col_index[i]][_] =0
            for _ in range(m):
                matrix[_][row_index[i]] =0
    return matrix 

arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setmetrix(arr)
            