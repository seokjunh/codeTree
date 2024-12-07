gender = int(input())
age = int(input())

if age >= 19:
    if gender == 0:
        print("M")
    else:
        print("W")
else:
    if gender == 0:
        print("B")
    else:
        print("G")