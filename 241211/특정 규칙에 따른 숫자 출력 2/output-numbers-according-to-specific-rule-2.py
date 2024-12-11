n = int(input())

arr = [9,7,5,3,1]

k = 0

for _ in range(n):

    for _ in range(n):
        print(arr[k%5], end=" ")
        k += 1
    print()