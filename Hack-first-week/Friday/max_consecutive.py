from group import group


def max_consecutive(example_list):
    resulting_list = group(example_list)
    max_count = 0
    for current_list in resulting_list:
        if len(current_list) > max_count:
            max_count = len(current_list)
    print(resulting_list)
    return max_count

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
