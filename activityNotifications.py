# Complete the activityNotifications function below.
import bisect
def activityNotifications(expenditure, d):
    count = 0
    sub_array = sorted(expenditure[0:d])
    m = medium(sub_array, d)


    for i in range(d, len(expenditure)):
        if expenditure[i] >= m * 2:
            count += 1
        insert_x = expenditure[i]
        delete_x = expenditure[i-d]
        delete_pos = get_index(sub_array, delete_x)
        del sub_array[delete_pos]
        bisect.insort(sub_array, insert_x)
        m = medium(sub_array, d)
    return count

def get_index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def medium (arr,d):
    if d % 2 == 0:
        return float((arr[d//2 - 1] + arr[d//2]) / 2)
    else:
        return float(arr[d//2])


print(activityNotifications([2,3,4,2,3,6,8,4,5],5))

print(activityNotifications([10,20,30,40,50],3))










