import collections


board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

import collections
c = collections.defaultdict(dict)
c['a'].add(1)



def isvalid(board):
    rowhash = {}
    colhash = {}
    for row in range(9):
        for col in range(9):
            # print(rowhash,colhash)
            if board[row][col] == ".":
                continue
            
            if rowhash.get(row)  and board[row][col] in rowhash.get(row):
                return False
            else:
                if rowhash.get(row):
                    rowhash.get(row).add(board[row][col])
                else:
                    rowhash[row] =  set([board[row][col]])
            if colhash.get(col) and board[row][col] in colhash.get(col):
                return False
            else:
                if colhash.get(col):
                    colhash.get(col).add(board[row][col])
                else:
                    colhash[col] =  set([board[row][col]])
    return True


isvalid(board)



def isvalid(board):
    rowhash = collections.defaultdict(set)
    colhash = collections.defaultdict(set)
    square = collections.defaultdict(set)
    for row in range(9):
        for col in range(9):
            # print(rowhash,colhash)
            if board[row][col] == ".":
                continue
            
            if board[row][col] in rowhash[row] or \
                board[row][col] in colhash[col] or \
                board[row][col] in square[(row//3,col//3)]:
                return False
            
            rowhash[row].add(board[row][col])
            colhash[col].add(board[row][col])
            square[(row//3,col//3)].add(board[row][col])
    return True

isvalid(board)