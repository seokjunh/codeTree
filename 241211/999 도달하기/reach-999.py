n = int(input())

arr = [1,n]

while True:
    c = arr[-1] + arr[-2]
    arr.append(c)
    if c > 999:
        print(*arr)
        break