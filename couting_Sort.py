def counting_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    min_val = min(arr)
    
    count_range = max_val - min_val + 1
    count = [0] * count_range

    for num in arr:
        count[num - min_val] += 1

    sorted_arr = []
    for i in range(count_range):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr

if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    sorted_data = counting_sort(data)
    print("Array ordenado:", sorted_data)
