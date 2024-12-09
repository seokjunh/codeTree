n = int(input())

m = 1000

i = 1
s = 0
while m >= 500:
    m = m - 2*i
    s += 2*i
    if m <= n:
        print(i, s)
        break
    i += 1