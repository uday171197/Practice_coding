


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
ans = []   
lastAnswer = 0   
arr = [[]for i in range(n)]
for i in queries:
    i = queries[0]
    action, i, v = list(map(int, i))
    idx = (i[1]^lastAnswer)%n
    if action ==1:
        arr[idx].append(v)
    else:
        # print(arr)
        
        lastAnswer = arr[idx][v%(len(arr[idx]))]
        ans.append(lastAnswer)
        
        