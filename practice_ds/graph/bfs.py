



def BFS(node,ans,visnode,adjlist):
    queue = []
    queue.append(node)
    while queue:
        queuenode = queue.pop(0)
        print('queuenode--------->',queuenode)
        adjnodes = adjlist[queuenode]
        ans.append(queuenode)
        visnode[queuenode] = 1
        for adjnode in adjnodes:
            if not visnode[adjnode]:
                queue.append(adjnode)
                visnode[adjnode] = 1
    return ans
                



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
    ans = []
    for node in range(1,n+1):
        
        if not visnode[node]:
            ans = BFS(node,ans,visnode,adjlist)
            print('ans------>',ans)
    
    print(ans)
    
main()