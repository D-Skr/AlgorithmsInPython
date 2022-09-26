def binary_itr(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target: return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


arr = [2, 5, 6, 7, 8, 11, 12, 44, 55]
target = 55

result = binary_itr(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Target element is present at index %d" % result)
else:
    print("Element is not present in array")