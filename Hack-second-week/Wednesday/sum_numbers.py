import sys


def sum_nums_from_file():
    filename = sys.argv[1]
    file_with_nums = open(filename, 'r')
    string_with_nums = file_with_nums.readline()
    return(nums_from_string(string_with_nums))


def nums_from_string(string):
    numbers_as_strings = string.split()
    numbers = []
    for num in numbers_as_strings:
        numbers.append(int(num))
    return sum(numbers)


def main():
    print(sum_nums_from_file())


if __name__ == '__main__':
    main()
