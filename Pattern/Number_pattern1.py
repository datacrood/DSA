n = int(input())
if n%2==0:
    middle = n//2
else:
    middle = n//2+1

val = 1
for i in range(middle-1):
    for j in range(1, n+1):
        print(5*i+val, end=" ")
        val+=1
    print()

val=1
for i in range(1, middle):
    for j in range(1, n+1):
        print(5*i+val, end=" ")
        val+=1
    print()
