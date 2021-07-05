first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
    
arr = {}
for [a,b,k] in queries:
    # i = queries[2]
    arr[f'{a}'] = (arr[f'{a}'] if f'{a}' in arr else 0)+k
    arr[f'{b+1}'] = (arr[f'{b+1}'] if f'{b+1}' in arr else 0)-k
s = 0
mx = 0
for j in range(1,n+1):
    # j=4
    r = arr[f'{j}'] if f'{j}' in arr else 0
    s = s +r
    print(arr[f'{j}'] if f'{j}' in arr else 0,"----after addition -----------",s)
    if mx<s:
        mx = s
        print('max',mx)
print(mx)
