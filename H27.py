
def sqrt_sort(arr):
    sqrt = int(len(arr) ** (0.5))
    start = 0

    subgroups = []
    result_arr = []
    for stop in range(sqrt,len(arr)+1,sqrt):
        subgroups.append(arr[start:stop])
        start = stop
       
    while subgroups != []:
        searh_mini = []
        count = 0
        for i in subgroups:
            searh_mini.append(minimum(i)[0])
            count+=1
        mini = minimum(searh_mini)
        result_arr.append(mini[0])
        subgroups[mini[1]].remove(mini[0])
        if subgroups[mini[1]] == []:
            del subgroups[mini[1]]
    return result_arr



def minimum(arr): 
    mini = arr[0]
    sub = count = 0       
    for i in arr[1:]:
        count+=1
        if i < mini:
            mini = i
            sub = count
    return [mini,sub]

a = [ 13, 23, 56, 0, 12, 11, 24, 47, 2]
print(sqrt_sort(a))
