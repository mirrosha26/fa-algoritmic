def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

a = [1, 2, 56, 34, 12, 57, 24, 47, 80, 34, 237, 9, 93]
selection_sort(a)
print(a)