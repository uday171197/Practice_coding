
def dfs(node,visnode,ans,adjlist):
    print('node--------->',node)
    ans.append(node)
    visnode[node] = 1
    adjnodes = adjlist[node]
    for adjnode in adjnodes:
        if not visnode[adjnode]:
            ans = dfs(adjnode,visnode,ans,adjlist)
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
            ans = dfs(node,visnode,ans,adjlist)
    print('ans------------->',ans)
            
main()