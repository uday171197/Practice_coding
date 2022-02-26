
from operator import truediv

from numpy import True_


def dfs_cyclic(node,visnode,adjlist,previous_node):
    
    
    visnode[node] = 1
    adjnodes = adjlist[node]
    for adjnode in adjnodes:
        print(adjnode,previous_node)
        if not visnode[adjnode]:
            if dfs_cyclic(adjnode,visnode,adjlist,node):
                return True
        elif adjnode != previous_node:
            return True_
    return False


def main():
    n = int(input('Enter no of node : '))
    e = int(input('Enter no of edge : '))
    adjlist = [[] for i in range(n+1)]
    for i in range(e):
        print(f'u and v value for ({i}): ') 
        u,v = [int(i) for i in input().split()]
        adjlist[u].append(v)
        adjlist[v].append(u)
    print('adjlist------------>',adjlist)
    visnode = [0 for i in range(n+1)]
    for node in range(1,n+1):
        if not visnode[node]:
            ans = dfs_cyclic(node,visnode,adjlist,-1)
        if ans:
            print(' This is cyclic graph')
            break
        
    if not ans:
        print('This in not cyclic graph')
            
main()