n = int(input())

arr = list(map(int,input().split()))

d = {}

for i in arr:
    
    if i < 100:
        if "0" not in d:
            d["0"] = 1
        else:
            d["0"] += 1
    
    else:
        s = str(i)[0]
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1

for key, value in sorted(d.items()):
    print(key,"-",value)