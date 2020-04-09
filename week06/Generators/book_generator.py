from random import randint


def random_char():
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    rand = randint(0, 25)

    return char[rand]


def random_word():
    rand_length = randint(1, 15)
    res = ''
    for i in range(rand_length):
        res += ''.join(random_char())

    return res

def random_line():
    rand = randint(1,22)
    return rand % 2 == 0


def genarte_book(chapter_count, chapter_length):
    for chapter in range(1, chapter_count + 1):
        with open('book.txt', 'a') as f:
            f.write('# Chapter ' + str(chapter) + '\n')
            for i in range(chapter_length):
                f.write(random_word() + ' ')

            f.write('\n\n')

        yield chapter

from book_reader import *

def main():
    chapters = 3
    chapter_length = randint(100, 200)

    book = genarte_book(chapters, chapter_length)
    for i in range(chapters):
        next(book)
        
    # for chapter in book_reader('book.txt'):
    #     print('Press enter to continue reading')
    #     input()
    #     clear_screen()
    #     print(chapter)


if __name__ == '__main__':
    main()
