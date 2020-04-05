import sys


def cat(arguments):
    with open(arguments, 'r') as f:
        return f.read()


def main():
    print(cat(sys.argv[1]))


if __name__ == '__main__':
    main()
