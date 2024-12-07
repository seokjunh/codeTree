a, b = map(int, input().split())

if a > b:
    for i in range(a,b-1,-1):
        for j in range(1,10,3):
            print(i,"*",j,"=",i*j,"",i,"*",(j+1),"=",i*(j+1),"",i,"*",(j+2),"=",i*(j+2))
        print()
else:
    for i in range(a,b+1):
        for j in range(1,10,3):
            print(i,"*",j,"=",i*j,"",i,"*",(j+1),"=",i*(j+1),"",i,"*",(j+2),"=",i*(j+2))
        print()