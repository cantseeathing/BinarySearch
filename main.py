import math


def binarySearch(sorted_array, value):
    start = 0
    end = len(sorted_array) - 1
    middle = math.floor((start + end) / 2)
    # print(start, middle, end)
    while not (sorted_array[middle] == value) and start<=end:
        if value < sorted_array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
    if sorted_array[middle] == value:
        return middle
    else:
        return -1


cust_array = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(cust_array, 9))
