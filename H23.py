def merge(a:list, b:list):
    return_list = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            return_list.append(a[i])
            i += 1
        else:
            return_list.append(b[j])
            j += 1
    if i < len(a):
        return_list += a[i:]
        i += 1
    if j < len(b):
        return_list += b[j:]
        j += 1
    #print(a, ' + ', b, ' = ', return_list )
    return return_list

# merge_sort(a: list) -> list
def merge_sort(this_list: list):
    if len(this_list) == 1:
        return this_list
    middle = len(this_list) // 2
    left = merge_sort(this_list[:middle])
    right = merge_sort(this_list[middle:])
    return merge(left,right)

print(merge_sort([1,9,8,2,10,14,3,45,56,76]))