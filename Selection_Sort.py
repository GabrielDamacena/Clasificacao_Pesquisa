def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

arr1 = [1, 3, 6, 9, 10, 23, 45]
selection_sort(arr1)
print(arr1)
    
arr2 = [45, 23, 10, 9, 6, 3, 1]
selection_sort(arr2)
print(arr2)    
    
arr3 = [1, 3, 3, 6, 6, 9, 9]
selection_sort(arr3)
print(arr3)    

arr4 = [10, 5, 2, 8, 7, 1]
selection_sort(arr4)
print(arr4)