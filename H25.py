def bubble_sort(array):
    stop = -len(array) -1
    for i in range(-1, stop, -1):
        range(-1, stop - i, -1)
        for j in range(-1, stop - i, -1):
            print(str(i), (j))
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
 
a = [1, 2, 56, 34, 12, 57, 24, 47, 80, 34, 237, 9, 93]
bubble_sort(a)
print(a)