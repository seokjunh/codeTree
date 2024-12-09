n = int(input())

num = 9
m = num-n

while num > m:
    for i in range(num, num-n, -1):
        if i <= 0:
            print(1, end=" ")
        else:
            print(i, end=" ")
    print()
    num -= 1