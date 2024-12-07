h, w = map(int, input().split())

bmi = (w*(100**2)) // (h**2)

print(bmi)
if bmi >= 25:
    print("Obesity")