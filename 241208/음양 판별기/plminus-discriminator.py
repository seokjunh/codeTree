n = int(input())

for _ in range(n):
    c = int(input())

    if c < 0:
        print("minus")
    elif c > 0:
        print("plus")
    else:
        print("zero")