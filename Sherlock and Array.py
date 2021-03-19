# Complete the balancedSums function below.
def balancedSums(arr):
    leftSum = 0
    rightSum = sum(arr)
    for i in range(len(arr)):
        rightSum -= arr[i]
        if leftSum == rightSum:
            return "YES"
        else:
            leftSum += arr[i]
    return "NO"

print(balancedSums([5,6,7,11]))
print(balancedSums([1,2,3]))
print(balancedSums([1,2,3,3]))
print(balancedSums([1,1,4,1,1]))
print(balancedSums([2,0,0,0]))
print(balancedSums([0,0,2,0]))