import sys
import os


def find_size(path):
    try:
        sum_of_sizes = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for myfile in filenames:
                statinfo = os.stat(str(dirpath) + '/' + str(myfile))
                sum_of_sizes += statinfo.st_size
        return (sum_of_sizes) / (1024 * 1024)
    except Exception as error:
        return(str(error) + ' Sorry!')


def main():
    print('{0:.2f}'.format(find_size(sys.argv[1])))


if __name__ == '__main__':
    main()
# /home/desi/Desi's-Gluposti/Code/Learning-Python
