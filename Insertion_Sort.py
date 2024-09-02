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


