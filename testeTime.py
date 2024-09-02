import time

from bubble_Sort import bubble_sort
from Insertion_Sort import insert_sort
from Merge_Sort import merge_sort
from Selection_Sort import selection_sort


start_time_bubble = time.perf_counter()

arr1 = [1, 3, 6, 9, 10, 23, 45]
bubble_sort(arr1)

    
arr2 = [45, 23, 10, 9, 6, 3, 1]
bubble_sort(arr2)
 
    
arr3 = [1, 3, 3, 6, 6, 9, 9]
bubble_sort(arr3)


arr4 = [10, 5, 2, 8, 7, 1]
bubble_sort(arr4)


end_time_bubble = time.perf_counter()

execution_time_bubble = end_time_bubble - start_time_bubble

start_time_insert = time.perf_counter()
arr1 = [1, 3, 6, 9, 10, 23, 45]
insert_sort(arr1)

    
arr2 = [45, 23, 10, 9, 6, 3, 1]
insert_sort(arr2)
    
    
arr3 = [1, 3, 3, 6, 6, 9, 9]
insert_sort(arr3)
    

arr4 = [10, 5, 2, 8, 7, 1]
insert_sort(arr4)

end_time_insert = time.perf_counter()

execution_time_insert = end_time_insert - start_time_insert


start_time_merge = time.perf_counter()
arr1 = [1, 3, 6, 9, 10, 23, 45]
merge_sort(arr1)

    
arr2 = [45, 23, 10, 9, 6, 3, 1]
merge_sort(arr2)

    
arr3 = [1, 3, 3, 6, 6, 9, 9]
merge_sort(arr3)


arr4 = [10, 5, 2, 8, 7, 1]
merge_sort(arr4)

end_time_merge = time.perf_counter()

execution_time_merge = end_time_merge - start_time_merge

start_time_section = time.perf_counter()
arr1 = [1, 3, 6, 9, 10, 23, 45]
selection_sort(arr1)

    
arr2 = [45, 23, 10, 9, 6, 3, 1]
selection_sort(arr2)

    
arr3 = [1, 3, 3, 6, 6, 9, 9]
selection_sort(arr3)


arr4 = [10, 5, 2, 8, 7, 1]
selection_sort(arr4)

end_time_selection = time.perf_counter()

execution_time_selection = end_time_selection  - start_time_section



print(f"Tempo de execução bubble: {execution_time_bubble} segundos")
print(f"Tempo de execução bubble: {execution_time_insert} segundos")
print(f"Tempo de execução bubble: {execution_time_merge} segundos")
print(f"Tempo de execução bubble: {execution_time_selection} segundos")