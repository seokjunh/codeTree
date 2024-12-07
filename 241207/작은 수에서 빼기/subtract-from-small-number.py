a, b = map(int, input().split())

if a > b:
    temp = a
    a = b
    b = temp

print(a-b)
