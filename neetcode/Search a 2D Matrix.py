def binarySearch(row,t):
    l,r = 0,len(row)
    while l<r:
        m = (l+r-1)//2
        if row[m] < target:
            l = m+1
        elif row[m] > target:
            r = m-1
        else:
            return True



def searchMatrix(matrix,target):
    for row in matrix:
        res = binarySearch(row,target)
        if res:
            return True
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 15

searchMatrix(matrix,target)