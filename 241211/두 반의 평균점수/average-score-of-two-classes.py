n = int(input())

arr = list(map(int, input().split()))

x, y = map(int, input().split())

avg = (arr[x-1] + arr[y-1])/2

print(format(avg, ".1f"))