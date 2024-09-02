import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        
        merge_sort(left_half)
        merge_sort(right_half)

        
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1



arr1 = [1, 3, 6, 9, 10, 23, 45]
merge_sort(arr1)
print(arr1)
    
arr2 = [45, 23, 10, 9, 6, 3, 1]
merge_sort(arr2)
print(arr2)    
    
arr3 = [1, 3, 3, 6, 6, 9, 9]
merge_sort(arr3)
print(arr3)    

arr4 = [10, 5, 2, 8, 7, 1]
merge_sort(arr4)
print(arr4)




