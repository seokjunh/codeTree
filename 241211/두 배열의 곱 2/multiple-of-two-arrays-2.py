arr1 = []
arr2 = []

for _ in range(4):
    arr1.append(list(map(int, input().split())))

for _ in range(5):
    l = list(map(int, input().split()))
    if not l:
        continue
    arr2.append(l)

for i in range(4):
    for j in range(2):
        print(arr1[i][j]*arr2[i][j], end=" ")
    print()