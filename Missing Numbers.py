
# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    dict = {}
    result = []
    for i in range(len(arr)):
        dict[arr[i]] = dict.get(arr[i], 0) - 1
        dict[brr[i]] = dict.get(brr[i], 0) + 1

    for i in range(len(arr), len(brr)):
        dict[brr[i]] = dict.get(brr[i], 0) + 1

    for k in dict.keys():
        if dict[k] > 0:
            result.append(k)

    result.sort()
    return result


print(missingNumbers([203,204,205,206,207,208,203,204,205,206],[203,204,204,205,206,207,205,208,203,206,205,206,204]))













