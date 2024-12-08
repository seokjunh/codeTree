n = int(input())

for _ in range(n):
    c = int(input())

    if c == 0:
        break

    if c % 3 == 0:
        print(c//3)
    else:
        print(c+2)
