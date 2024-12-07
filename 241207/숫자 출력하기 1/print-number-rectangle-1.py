n, m = map(int, input().split())

i = 1
for j in range(1, n*m+1):
    if j == m*i:
        print(j)
        i += 1
    else:
        print(j, end=" ")
    
    