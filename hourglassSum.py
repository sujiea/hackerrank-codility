def hourglassSum(arr):
    sum_max = -64
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            sum_a = arr[i][j] + arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum_max < sum_a:
                sum_max = sum_a
    return sum_max



print(hourglassSum([[-1,-1,0 -9 -2 -2],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]))


