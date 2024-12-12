n = int(input())

arr = [[] for _ in range(n)]
for i in range(1,n+1):
    for _ in range(i):
        arr[i-1].append(2)


for i in range(2,n):
    for j in range(1,len(arr[i])-1):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in arr:
    print(*i)