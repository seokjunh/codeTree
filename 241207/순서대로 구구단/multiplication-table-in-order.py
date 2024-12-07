a, b = map(int, input().split())

for j in range(1,10):
    for i in range(a,b+1):
        print(i,"*",j,"=",i*j, end="  ")
    print()