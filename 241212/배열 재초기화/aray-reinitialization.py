n = int(input())

for i in range(n):
    l = list(map(int, input().split()))
    if i % 2 == 0:
        for j in range(n):
            if j % 2 != 0:
                l[j] = 2
            else:
                l[j] = 1
        print(*l)
    else:
        for j in range(n):
            if j % 2 != 0:
                l[j] = 2
        print(*l)