n = int(input())
m = int(input())

s = str(m)[::-1]

for i in s:
    c = int(i)
    print(n*c)

print(n*m)