itemAssociation =[
    ['Item1', 'Item2'],
    ['Item2', 'Item5'],
    ['Item3', 'Item4'],
    ['Item4', 'Item5']
]

import copy
import queue

d= {}
group = []
for item in itemAssociation:
    print(item)
    if item[0] in d:
        group[d[item[0]]].extend(item[1:])
    else:
        group.append(item)
        d[item[-1]] = len(d)
        
max = 0
ans = []
for i in group:
    if len(i) > max:
        ans = i
        max= len(i)
    elif len(i) == max:
        if ans[0][0] > i[0][0]:
            ans = i
            
        else:
            pass
    else:
        pass
    
    
# creating dfs solustion
            


def groupItemAssociation(itemAssociation):

    
    uniqueitems = []
    for i in itemAssociation:
        uniqueitems.extend(i)
    uniqueitems = list(set(uniqueitems))
    uniqueitems.sort(key=lambda x:x[-1])
    visnode = {i:0 for i in uniqueitems}
    adjlist = {i:[] for i in uniqueitems}
    for  item in itemAssociation:
        if adjlist.get(item[0]):
            adjlist[item[0]].append(item[1])
        elif adjlist.get(item[1]):
            adjlist[item[1]].append(item[0])
        else:
            adjlist[item[0]] = [item[1]]
            adjlist[item[1]] = [item[0]]
        
            
    max = 0
    ansitem = []
    for i in uniqueitems:
        
        if not visnode[i]:
            ans = []
            queue = []
            queue.append(i)
            while queue:
                queuenode = queue.pop(0)
                ans.append(queuenode)
                visnode[queuenode] = 1
            
                ajdnodes = adjlist.get(queuenode)
                if ajdnodes:
                    for j in ajdnodes:
                        if not visnode[j]:
                            queue.append(j)
                            visnode[j] = 1
            # print('ans------->',ans)
            if len(ans) > max:
                ansitem = ans
                max = len(ans)

    return ansitem

itemAssociation =[
    ['Item1', 'Item2'],
    ['Item2', 'Item5'],
    ['Item3', 'Item4'],
    ['Item4', 'Item5']
]

groupItemAssociation(itemAssociation)


