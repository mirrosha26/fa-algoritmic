def merge(first_list, second_list):
    return_list = []
    i, j = 0, 0
    while i < len(first_list) and j < len(second_list):
        if first_list[i] <= second_list[j]:
            return_list.append(first_list[i])
            i += 1
        else:
            return_list.append(second_list[j])
            j += 1
    while i < len(first_list):
        return_list.append(first_list[i])
        i += 1
    while j < len(second_list):
        return_list.append(second_list[j])
        j += 1
    return return_list

list_1 = [1,3,4,6,8,14,45]
list_2 = [2,6,8,14,46]
print(merge(list_1, list_2))