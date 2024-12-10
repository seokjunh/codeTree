n = int(input())

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(1,n+1-i):
        print(k,end=" ")
    print()