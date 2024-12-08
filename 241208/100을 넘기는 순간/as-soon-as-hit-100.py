n = int(input())

arr = list(map(int, input().split()))

total = 0
cnt = 0
for i in arr:
    if i >= 100:
        total += i
        cnt += 1
        break
    total += i
    cnt += 1

print(total)
print(format(total/cnt, ".1f"))