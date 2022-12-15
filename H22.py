def intersection(a: list, b: list):
    return_list = []
    i,j = 0,0 
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            return_list.append(a[i])
            i+=1
            j+=1
        else:
            if a[i] < b[j]:
                i+=1
            else: 
                j+=1
    return return_list

a = [1,3,4,6,8,14,45]
b = [2,6,8,14,15,35,45,46,69,75]
print(intersection(a,b)) 
