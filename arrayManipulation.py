def arrayManipulation(n, queries):
    arr_add = [0] * (n + 2)
    for i in range(len(queries)):
        arr_add[queries[i][0]] += queries[i][2]
        arr_add[queries[i][1] + 1] -= queries[i][2]

    max_sum = 0
    cur_sum = 0
    for i in range(len(arr_add)):
        cur_sum += arr_add[i]
        max_sum = max(cur_sum, max_sum)

    return max_sum

print(arrayManipulation(4,[[2,3,603],[1,1,286],[4,4,882]]))

print(arrayManipulation(40,[[19,28,419], [4,23,680], [5,6,907], [19,33,582], [5,9,880], [10,13,438], [21,39,294], [13,18,678], [12,26,528], [15,30,261], [8,9,48], [21,23,131], [20,21,7], [13,40,65], [13,23,901], [15,15,914], [14,35,704], [20,39,522], [10,18,379], [16,27,8], [25,40,536], [5,9,190], [1,7,20,809], [8,20,453], [22,37,298], [19,37,112], [2,5,186], [21,29,184], [23,30,625], [2,8,960]]))


print(arrayManipulation(10,[[1,5,3],[4,8,7],[6,9,1]]))
print(arrayManipulation(5,[[1,2,200],[2,5,100],[3,4,100]]))



