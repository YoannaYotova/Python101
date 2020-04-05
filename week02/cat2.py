# cat2.py
import sys


def cat2(arguments):
    with open(arguments, 'r') as f:
        return f.read()


def main():
    for i in range(1, len(sys.argv)):
        print(cat2(sys.argv[i]))
        if i != len(sys.argv) - 1:
            print('\n')


if __name__ == '__main__':
    main()
