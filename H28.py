def sort_iter(list_arr):
    for i in range(-1, -len(list_arr), -1):
        value = list_arr[i]
        j = i
        while j > -len(list_arr) and list_arr[j - 1] > value:
            list_arr[j] = list_arr[j - 1]
            j = j - 1
        list_arr[j] = value
 
l = [3, 8, 5, 4, 1, 9, -2]
sort_iter(l)
print(l)