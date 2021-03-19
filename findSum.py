def findSum(numbers, queries):
    # Write your code here
    result = []
    n = len(numbers)
    sum_arr = [0] * (n +1)
    zero_sum = [0] * (n +1)
    sum = 0
    zero = 0
    for i in range(n):
        sum += numbers[i]
        if numbers[i] == 0:
            zero += 1
        sum_arr[i+1] = sum
        zero_sum[i+1] = zero

    for q in queries:
        sum = sum_arr[q[1]] - sum_arr[q[0]-1]
        zero_num = zero_sum[q[1]] - zero_sum[q[0]-1]
        sum += zero_num * q[2]
        result.append(sum)
    return result

print(findSum([-5,0], [[2,2,20],[1,2,10]]))
print(findSum([5,10,10], [[1,2,5]]))
print(findSum([20,30,0,10], [[1,3,10]]))


def findSum(numbers, queries):
    # Write your code here
    result = []
    for q in queries:
        sum = 0
        for i in range(q[0] - 1, q[1]):
            if numbers[i] != 0:
                sum += numbers[i]
            else:
                sum += q[2]
        result.append(sum)
    return result














