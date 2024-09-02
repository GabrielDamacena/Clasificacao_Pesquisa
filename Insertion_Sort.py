import time
def insert_sort(data):
    n = len(data)

    if n <= 1:
        return
    
    for i in range(1, n):
        chave = data[i]
        j = i - 1
        
        while j >= 0 and chave < data[j]:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = chave

start_time = time.time()
arr1 = [1, 3, 6, 9, 10, 23, 45]
insert_sort(arr1)
print(arr1)
    
arr2 = [45, 23, 10, 9, 6, 3, 1]
insert_sort(arr2)
print(arr2)    
    
arr3 = [1, 3, 3, 6, 6, 9, 9]
insert_sort(arr3)
print(arr3)    

arr4 = [10, 5, 2, 8, 7, 1]
insert_sort(arr4)
print(arr4)
