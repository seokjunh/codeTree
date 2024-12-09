x, y = map(int, input().split())

if x > y:
    temp = x
    x = y
    y = temp

s = 0
cnt = 0
for i in range(x, y+1):
    if i % 5 != 0:
        s += i
        cnt += 1

avg = format(s/cnt, ".1f")

print(s, avg)