def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Exemplo de uso
arr = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
sorted_arr = quick_sort(arr)
print("Quick Sort:", sorted_arr)
