n = int(input())

arr = list(map(int, input().split()))

s = 0
cnt = 0

for i in arr:
    if i % 7 == 0:
        s += i
        cnt += 1

avg = format(s/cnt, ".1f")

print(cnt, s, avg)