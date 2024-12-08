n = int(input())

for _ in range(n):
    a,b,c = map(str, input().split())

    a = int(a)
    b = int(b)

    if c == "s":
        print(a*b)
    elif c == "t":
        print(format((a*b)/2, ".1f"))