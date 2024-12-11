n = int(input())

arr = list(map(int, input().split()))

s = 0
cnt = 0
for i in range(n):
    if i % 2 != 0:
        s += arr[i]
        cnt += 1

avg = format(s/cnt, ".1f")

print(s, avg)