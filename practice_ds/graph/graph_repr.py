
n = 5
m = 7

edges = [(1,2),(2,5),(2,4),(1,3),(3,4),(4,5),(1,4)]
adhelist = [[] for i in range(n+1)]
for u,v in edges:
    adhelist[u].append(v)
    adhelist[v].append(u)

