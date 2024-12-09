n, m = map(int, input().split())

cnt = 0
for i in range(n*m, 0, -1):
    if cnt == m:
        cnt = 0
        print()
        print(i, end=" ")
        cnt += 1
    else:
        print(i, end=" ")
        cnt += 1