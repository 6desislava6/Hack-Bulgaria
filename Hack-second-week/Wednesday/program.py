import sys


def read_file():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        textfile = open(filename, 'r')
        text = textfile.read()
        textfile.close()
        return text
    else:
        print('Give me the file!')


def main():
    print(read_file())
if __name__ == '__main__':
    main()
