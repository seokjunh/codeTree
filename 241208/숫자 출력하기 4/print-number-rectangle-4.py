n, k = map(int, input().split())

if k == 1:
    for i in range(1,n+1):
        for j in range(n):
            if j == n-1:
                print(i)
            else:
                print(i, end=" ")
elif k == 2:
    for i in range(n):
        if i % 2 == 0:
            for j in range(1,n+1):
                if j == n:
                    print(j)
                else:
                    print(j, end=" ")
        else:
            for j in range(n,0,-1):
                if j == 1:
                    print(j)
                else:
                    print(j, end=" ")
else:
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == n:
                print(i*j)
            else:
                print(i*j, end=" ")