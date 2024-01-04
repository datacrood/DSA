def findLargest(arr, nRows, mCols):
    sum_col=[]
    for col in range(mCols):
        summ=0
        for row in range(nRows):
            summ+=arr[row][col]
        sum_col.append(summ)
    max_col = float("-inf")
    for i in range(len(sum_col)):
        if sum_col[i]>max_col:
            max_col = sum_col[i]
            max_col_index = i
        
    sum_row = []
    for row in range(nRows):
        summ = 0
        for col in range(mCols):
            summ+=arr[row][col]
        sum_row.append(summ)
    max_row = float("-inf")
    for i in range(len(sum_row)):
        if sum_row[i]>max_row:
            max_row = sum_row[i]
            max_row_index = i

    if max_col==max_row:
        print("row", max_row_index, max_row)
    elif max_col>max_row:
        print("column", max_col_index, max_col)
    else:
        print("row", max_row_index, max_row)

m, n = 3,3
mat = [[1,2,3], [4,5,6], [7,8,9]]
findLargest(mat, m, n)
