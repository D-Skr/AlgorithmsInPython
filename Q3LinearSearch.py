def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


arr = [2, 3, 1, 5, 77, 6, 54, 11]
target = 6

print(search(arr, target))