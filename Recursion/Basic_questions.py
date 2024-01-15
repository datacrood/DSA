# Checking whether the array is sorted or not
def is_sorted(arr, n):
    if n==0:
        return True
    if arr[n]<arr[n-1]:
        return False
    return is_sorted(arr, n-1)


arr= [1,2,4,5,50, 90, 100]
n = len(arr)-1
print(is_sorted(arr, n))

#----------------------------------------------------------------------------------------
def findIndex(arr, i, x):
    n= len(arr)
    if i==n:
        return "Not found"
    if arr[i]==x:
        return i
    return findIndex(arr, i+1, x)


# Method-2
def findIndex1(arr, x,i):
    n = len(arr)
    if n==0:
        return "Not found"
    if arr[0]==x:
        return i
    arr=arr[1:]
    return findIndex(arr, x, i+1)

#Method-3
def findIndex2(arr, x):
    n = len(arr)
    if n==0:
        return "Not found"
    if arr[0]==x:
        return 0
    arr=arr[1:]
    output = findIndex(arr, x, i+1)
    if output=="Not found":
        return "Not found"
    else:
        return output+1 # Note: This is also doing the same i.e., adding 1 to zero everytime.

arr= [1,2,4,5,50, 90, 100]
print(findIndex(arr, 0, 7))
print(findIndex1(arr, 5, 0))
print(findIndex2(arr, 5))
