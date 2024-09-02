import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# start_time = time.time()
# arr1 = [1, 3, 6, 9, 10, 23, 45]
# bubble_sort(arr1)
# print(arr1)
    
# arr2 = [45, 23, 10, 9, 6, 3, 1]
# bubble_sort(arr2)
# print(arr2)    
    
# arr3 = [1, 3, 3, 6, 6, 9, 9]
# bubble_sort(arr3)
# print(arr3)    

# arr4 = [10, 5, 2, 8, 7, 1]
# bubble_sort(arr4)
# print(arr4)

# end_time = time.time()

# execution_time = end_time - start_time

# print(f"Tempo de execução: {execution_time} segundos")