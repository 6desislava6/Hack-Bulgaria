def groupby(func, seq):
    dict_grouped = {}

    for element in seq:
        if func(element) in dict_grouped:
            dict_grouped[func(element)].append(element)
        else:
            dict_grouped[func(element)] = [element]
    return dict_grouped

print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
