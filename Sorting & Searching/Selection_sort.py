def selectionSort(arr, n): 
    for i in range(n-1):
        mini = arr[i]
        smini = mini
        for k in range(i+1, n):
            if arr[k] < smini:
                smini = arr[k]
                flag = k
        if smini!=mini:
            arr[i], arr[flag] = arr[flag], arr[i]
    return arr

n = int(input())
arr = list(map(int, input().split(" ")))
# n = 7
# arr = [1, 9, 2, 3, 6, 4, 28]
print(selectionSort(arr, n))
