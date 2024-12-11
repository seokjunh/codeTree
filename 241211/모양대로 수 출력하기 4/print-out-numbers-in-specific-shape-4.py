n = int(input())

s = 0
for i in range(1,n+1):
    s += i

arr = [2,4,6,8]

k = 0

for i in range(n):

    for j in range(i):
        print(" ", end=" ")
    
    for _ in range(n-i):
        print(arr[k%4], end=" ")
        k += 1
    print()
    


    
    
