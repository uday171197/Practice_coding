


'''
this is the first solution which have time time complexity of 

TC = O(m*n) + O(m*n) + O(m*n)
SC = O(M+N)

'''

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def setZeroMetrix(matrix):
    rowm,coln = len(matrix),len(matrix[0])
    row = [-1]*rowm
    col = [-1]*coln
    for i in range(rowm):
        for j in range(coln):
            if matrix[i][j] == 0:
                row[i] = 0
                col[j] = 0
                
    # fil all row with zero
    i = 0
    for  i in range(rowm):
        if row[i] == 0: 
            for j in range(coln):
                matrix[i][j] = 0
    
    # fill all col with 0
    i = 0
    for  i in range(coln):
        if col[i] == 0: 
            for j in range(rowm):
                matrix[j][i] = 0
    return matrix

setZeroMetrix(matrix)
        
        
        
'''
solution2

'''


matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]

def setZeroMetrix(matrix):
    rowm,coln = len(matrix),len(matrix[0])
    for i in range(rowm):
        for j in range(coln):
            if matrix[i][j] == 0:
                matrix[i][0] = ''
                matrix[0][j] = ''
                
    # fil all row with zero
    for  i in range(rowm):
        if matrix[i][0] == '': 
            if i !=0:
                matrix[i][0] = 0
            for j in range(coln):
                if matrix[i][j] != '':
                    matrix[i][j] = 0
    
    # fill all col with 0
    for  i in range(coln):
        if matrix[0][i] == '': 
            matrix[0][i] = 0
            for j in range(rowm):
                if matrix[j][i] != '':
                    matrix[j][i] = 0
    return matrix

setZeroMetrix(matrix)
