def clear_screen():
    import os
    os.system('clear')


def book_reader(*args):
    for file in args:
        with open(f"Generators/{file}", 'r') as f:
            for line in f:
                if line[0] == '#':
                    yield line.strip()
                else:
                    print(line.strip())


for chapter in book_reader('001.txt', '002.txt'):
    print('Press enter to continue reading')
    input()
    clear_screen()
    print(chapter)
