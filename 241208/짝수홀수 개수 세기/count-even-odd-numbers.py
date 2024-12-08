n = int(input())

even = 0
odd = 0

for _ in range(n):
    c = int(input())
    if c == 0:
        break
    if c % 2 == 0:
        even += 1
    else:
        odd += 1

print(even)
print(odd)
