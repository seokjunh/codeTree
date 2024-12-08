n = int(input())
arr = list(map(int, input().split()))
k = int(input())

m = 0
d = 0

for i in arr:
    if k % i == 0:
        m += i
for i in arr:
    if i % k == 0:
        d += i

print(m)
print(d)