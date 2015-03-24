def group(example_list):
    resulting_list = []
    for i in range(0, len(example_list)):
        if i == 0:
            resulting_list.append([example_list[0]])
        elif example_list[i] == example_list[i-1]:
            resulting_list[len(resulting_list) - 1].append(example_list[i])
        else:
            resulting_list.append([example_list[i]])
    return resulting_list