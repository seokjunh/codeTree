n = int(input())

arr = list(map(str, input().split()))

d = {}

for i in arr:
    if i != "100":
        i = i[0] + "0"

    if int(i) not in d:
        d[int(i)] = 1
    elif int(i) in d:
        d[int(i)] += 1

for i,j in sorted(d.items(), reverse=True):
    print(i,"-",j)