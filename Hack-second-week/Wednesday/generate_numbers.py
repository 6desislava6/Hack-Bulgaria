from random import randint
import sys


def generate_random(count):
    numbers = []
    for x in range(int(count)):
        numbers.append(str(randint(1, 1000)))
    return numbers


def write_in_file():
    filename = sys.argv[1]
    file_to_be_written = open(filename, 'w')
    file_to_be_written.write(' '.join(generate_random(sys.argv[2])))


def main():
    write_in_file()


if __name__ == '__main__':
    main()
