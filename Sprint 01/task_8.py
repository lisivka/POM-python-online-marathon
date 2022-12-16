# TODO: task_8 +
"""
's3ooOOooDy' has exams. He wants to study hard this time.
He has an array of studying hours per day for the previous exams.
He wants to know the length of the maximum non-decreasing contiguous subarray
of the studying days, to study as much before his current exams.

Example:

For a = [2,2,1,3,4,1] the answer is 3.

[input] array.integer a
The number of hours he studied each day.

[output] integer
The length of the maximum non-decreasing contiguous subarray."""


def studying_hours(a):
    result = []
    count = 1
    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:
            count += 1
            print(a[i], ">=", a[i - 1], "+1", count)


        else:
            print("=======", count)
            result.append(count)
            count = 1
    result.append(count)

    print(result)
    return max(result)


a = [2, 2, 1, 3, 4, 1]
# a = [2, 2, 9]
print(studying_hours(a))
