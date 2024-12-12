n = int(input())

a,b = map(int,input().split())

arr = [a,b]

for i in range(2,n):
    s = arr[i-1] + arr[i-2]
    if len(str(s)) > 1:
        arr.append(int(str(s)[-1]))
    else:       
        arr.append(s)

print(*arr)