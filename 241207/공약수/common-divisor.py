n = int(input())

arr = list(map(int, input().split()))
arr.sort()

s = set()
for i in range(1, arr[0]+1):
    cnt = 0
    for j in arr:
        if j % i == 0:
            cnt += 1
    if cnt == len(arr):
        s.add(i)

for i in s:
    print(i)
