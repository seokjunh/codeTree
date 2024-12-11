n = int(input())

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        print(i-6, i)
        print(sum(arr[i-6:i]))