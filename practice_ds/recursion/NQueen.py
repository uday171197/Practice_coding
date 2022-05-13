def isvalidplace(board,row,col,n):
    mainrow = row
    maincol = col
    
    # checking for left all row
    while row > 0:
        if board[row][col] == 'Q':
            return False
        row-=1
    
    # checking for left downword daigonal
    row = mainrow
    col = maincol
    while row > 0 and col > 0:
        if board[row][col] == 'Q':
            return False
        row-=1
        col-=1
        
    # checking for left upword daigonal
    row = mainrow
    col = maincol
    while row > 0 and col < n:
        if board[row][col] == 'Q':
            return False
        row-=1
        col+=1
    return True
    
        
        
        


def findNqueue(board,n,row,col,res):
    if row == n:
        res+=1
        print(res)
        return
    
    for row in range(row,n):
        if isvalidplace(board,row,col,n):
            board[row][col] = 'Q'
            findNqueue(board,n,row,col+1,res)
            board[row][col] = '.'
        



def main():
    n = 6
    board = []
    for i in range(n):
        board.append(['.']*n)
    findNqueue(board,0,0,0,0)
main()
