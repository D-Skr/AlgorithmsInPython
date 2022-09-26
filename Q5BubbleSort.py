def bubble_optimized(arr):
    iterations = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            iterations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, iterations


arr = [82, 1, 4, 5, 2, 7, 7, 4, 56]
print(bubble_optimized(arr))