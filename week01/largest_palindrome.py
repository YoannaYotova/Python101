def is_it_palinrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def get_largest_palindrome(number):
    previous_num = number - 1
    while is_it_palinrome(str(previous_num)) is False:
        previous_num -= 1

    return previous_num


def main():
    number = 754649
    print(get_largest_palindrome(number))


if __name__ == '__main__':
    main()
