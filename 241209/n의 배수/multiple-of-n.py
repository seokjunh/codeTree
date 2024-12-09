n = int(input())


for i in range(n, 200):
    if i % n == 0 and i % 10 == 0:
        print(i)
        break
    if i % n == 0:
        print(i, end=" ")