arr1 = [8,5,2]
arr2=[1,3]
n, m = 3, 2
output = [0]*(3+ 1)

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    sum=0
    n = len(arr1)
    m = len(arr2)
    if n<m:
        while n<m:
            arr1.append(0)
            n = len(arr1)
            for i in range(n-1):
                arr1[-2-i], arr1[-1-i] = arr1[-1-i], arr1[-2-i]
    elif n>m:
        while n>m:
            arr2.append(0)
            m = len(arr2)
            for i in range(m-1):
                arr2[-2-i], arr2[-1-i] = arr2[-1-i], arr2[-2-i]
    
    for i in range(n):
        sum+= arr1[-1-i]+arr2[-1-i]
        last_digit= 0
        if sum>9:
            last_digit = sum%10
            output[-1-i]=last_digit
            sum=1
        else:
            output[-1-i] = sum
            sum=0
    if sum==1:
        output[0]= 1
    else:
        output[0]=0
    print(output)
sumOfTwoArrays(arr1, n, arr2, m, output)
