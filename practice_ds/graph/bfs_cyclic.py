



def BFS(node,ans,visnode,adjlist):
    queue = []
    queue.append(node)
    while queue:
        queuenode = queue.pop(0)
        # print('queuenode--------->',queuenode)
        adjnodes = adjlist[queuenode]
        visnode[queuenode] = 1
        for adjnode in adjnodes:
            if adjnode in queue:
                return True
            elif not visnode[adjnode]:
                queue.append(adjnode)
                visnode[adjnode] = 1
    return False

def BFSmethod2(node,ans,visnode,adjlist):
    queue = []
    queue.append((node,-1))
    while queue:
        queuenode = queue.pop(0)
        print('queuenode--------->',queuenode)
        adjnodes = adjlist[queuenode[0]]
        visnode[queuenode[0]] = 1
        for adjnode in adjnodes:
            if not visnode[adjnode]:
                print(adjnode, queuenode[1])
                queue.append((adjnode,queuenode[0]))
                visnode[adjnode] = 1
            elif adjnode != queuenode[1]:
                return True
                
                
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
    ans = []
    for node in range(1,n+1):
        if not visnode[node]:
            ans = BFS(node,ans,visnode,adjlist)
            if ans:
                print(' This is cyclic graph by method 1')
                break
    if not ans:
        print('This in not cyclic graph method 1')
        
    visnode = [0 for i in range(n+1)]
    for node in range(1,n+1):
        if not visnode[node]:
            ans = BFSmethod2(node,ans,visnode,adjlist)
            if ans:
                print(' This is cyclic graph by method 2')
                break
    if not ans:
        print('This in not cyclic graph by method 2')
    
main()