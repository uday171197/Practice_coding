def isvalidNode(node,color,m,graph,colors):
    for j in range(m):
        if j != node and graph[node][j] == 1 and colors[j] == color:
            return False
    return True
            


def solution(node,color,m,graph,colors,count):
    
    if node == m:
        count +=1
        print(count)
        return True
    
    for col in range(1,color+1):
        if isvalidNode(node,col,m,graph,colors):
            colors[node] = col
            # print(node,colors)
            solution(node+1,col,m,graph,colors,count)
            colors[node] = 0
    return False


colorvalues = 3
m = 4

graph = [
        [0,1,1,1],
        [1,0,1,0],
        [1,1,0,1],
        [1,0,1,0]
    ]

solution(0,colorvalues,m,graph,[0]*m,0)
