

def max_dct(dicts):
    return_dict = {}
    go_dicts = dicts[:]

    for a_dict in go_dicts:
            for key, value in a_dict.items():
                for b_dict in go_dicts:
                    if b_dict != a_dict:
                        if key in b_dict:
                            if value <= b_dict[key]:
                                return_dict[key] = b_dict[key]
                        else:
                            return_dict.setdefault(key, value)
    return return_dict

def sum_dct(dicts):
    return_dict = {}
    go_dicts = dicts[:]
    for a_dict in go_dicts:
            for key, value in a_dict.items():
                value_sum = value
                for b_dict in go_dicts:
                    if b_dict != a_dict:
                        if key in b_dict:
                                value_sum += b_dict[key]
                return_dict.setdefault(key, value_sum)
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
print(test)