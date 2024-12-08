n = int(input())

total = 0
for _ in range(n):
    c = int(input())
    total += c

avg = float(format(total/n, ".1f"))
print(avg)

if avg < 70:
    print("fail")