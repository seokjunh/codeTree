n = int(input())

arr = list(map(int, input().split()))

a,b = 0,0

for i in arr:
    if i % 5 == 0:
        a += 1
for i in arr:
    if i % 7 == 0:
        b += 1

print(a)
print(b)