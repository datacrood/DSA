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
