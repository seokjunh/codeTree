n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print("("+str(i**2)+","+str(j**2)+")", end=" ")
    print()