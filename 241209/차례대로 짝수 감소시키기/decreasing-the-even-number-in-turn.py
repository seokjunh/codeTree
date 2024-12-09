n = int(input())

m = 1000

i = 0
s = 0
while m >= 500:
    if m < n:
        print(i, s)
        break
    m = m - 2*i
    s += 2*i
    i += 1