def insertionSort(arr):
    for s in range(len(arr)-1):
        k=0
        for j in range(s+1):
            if arr[s-j]>arr[s+1-k]:
                arr[s-j], arr[s+1-k]=arr[s+1-k], arr[s-j]
                k+=1
    return arr
# A different approach then traditional ones.
