def max_dct(dicts):
    return_dict = {}
    for this_dict in dicts:
        for key, value in this_dict.items():
            value_t = return_dict.setdefault(key, value)
            if value_t < value:
                return_dict[key] = value
    return return_dict
    

def sum_dct(dicts):
    return_dict = {}
    for this_dict in dicts:
        for key, value in this_dict.items():
            return_dict.setdefault(key, 0)
            return_dict[key] += value
    return return_dict


test = [
            { 'a': 42, 'b': 5, 'f':6, 'm': 0},
            { 'k': 4, 'l': 54},
            { 'a': 14, 'i': 3, 'f':10, 'm': 2},
            { 'i': 3, 'l': 7, 'a':2, 'h': 23},
        ]
print(test)
print(max_dct(test))
print(sum_dct(test))