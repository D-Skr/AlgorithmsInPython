def insert_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


arr = [43, 6, 23, 43, 54, 44, 21, 443, 5, 3, 0, -100, 9]
print(insert_sort(arr))