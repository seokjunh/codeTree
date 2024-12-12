n = int(input())

arr = list(map(int, input().split()))

d = {}

for i in range(1,9):
    if i in arr:
        d[i] = arr.count(i)
    else:
        d[i] = 0

for i,j in sorted(d.items()):
    print(i,"-",j)
    
    