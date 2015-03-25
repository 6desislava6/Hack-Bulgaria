import sys

def main():
    open_and_print_mult_files()


def open_and_print_mult_files():
    if len(sys.argv) > 1:
        for index in range(1, len(sys.argv)):
            filename = sys.argv[index]
            textfile = open(filename, 'r')
            print(textfile.read())
            print('THIS IS THE END OF A FILE!')
            textfile.close()
    else:
        print('Give me the file!')


if __name__ == '__main__':
    main()
