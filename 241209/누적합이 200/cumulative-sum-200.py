n = int(input())

arr = list(map(int, input().split()))

s = 0
for i in range(len(arr)):
    s += arr[i]
    if s > 200:
        print(s)
        avg = format(s/(i+1), ".1f")
        print(avg)
        break