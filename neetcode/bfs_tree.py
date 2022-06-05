

def DFS(node,isvisited,adjlist,ans):
    print(node)
    ans.append(node)
    isvisited[node] = 1
    adjnodes = adjlist[node]
    for adjnode in adjnodes:
        if not isvisited[adjnode]:
            ans = DFS(adjnode,isvisited,adjlist,ans)
    return ans







def main():
    node = int(input('Enther the no. of node : '))
    edge= int(input('Enter no of edge : '))
    adjlist = [[] for i in range(edge+1)]
    for i in range(edge):
        u,v = input('Enter edge between nodes (u and v) :').split()
        adjlist[int(u)].append(int(v))
        adjlist[int(v)].append(int(u))
    isvisited= [0]*(node+1)
    ans = []
    for i in range(1,node+1):
        if not isvisited[i]:
            ans = DFS(i,isvisited,adjlist,ans)
    print(ans)