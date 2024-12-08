n = int(input())

arr = list(map(int, input().split()))

total = 0
cnt = 0

for i in arr:
    if i % 5 != 0 and i % 7 != 0:
        total += i
        cnt += 1

print(total)
print(format(total/cnt, ".1f"))