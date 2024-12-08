n = int(input())

arr = list(map(int, input().split()))

print(sum(arr))
print(format(sum(arr)/n, ".1f"))