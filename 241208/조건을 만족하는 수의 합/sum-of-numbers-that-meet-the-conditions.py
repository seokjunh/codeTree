n = int(input())

total = 0
for i in range(n, 501):
    if i % 2 == 0:
        total += i

print(total)