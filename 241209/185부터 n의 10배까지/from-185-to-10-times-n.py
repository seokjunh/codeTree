n = int(input())

s = 0
for i in range(185, n*10+1):
    s += i

avg = format(s/(n*10-184), ".1f")

print(s, avg)
