n = int(input())

alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

c = 0
for i in range(n,0,-1):

    for _ in range(i):
        print(alpabet[c%26],end="")
        c +=1
    print()