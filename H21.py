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
    while i < len(a):
        return_list.append(a[i])
        i += 1
    while j < len(b):
        return_list.append(b[j])
        j += 1
    return return_list

a = [1,3,4,4,6,8,14,45]
b = [2,6,8,8,14,44,44,46]

print(*merge(a, b))