def anagrams():
    first_string = input('First word: ')
    second_string = input('Second word: ')

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string_in_list = [i for i in first_string]
    second_string_in_list = [i for i in second_string]

    first_string_in_list.sort()
    second_string_in_list.sort()

    if first_string_in_list == second_string_in_list:
        print('ANAGRAMS')
    else:
        print('NOT ANAGRAMS')


def main():
    anagrams()


if __name__ == '__main__':
    main()
