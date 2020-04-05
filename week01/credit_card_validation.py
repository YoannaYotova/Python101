def sum_of_digits(n):
    string = str(n)
    sum = 0
    for digit in string:
        sum = sum + int(digit)

    return sum


def is_credit_card_valid(credit_card):
    str_credit_card = str(credit_card)
    list_credit_card = list(str_credit_card[::-1])
    if len(list_credit_card) % 2 == 0:
        raise ValueError('Invalid credit card')

    for i in range(1, len(list_credit_card), 2):
        list_credit_card[i] = str(int(list_credit_card[i]) * 2)
    number = int("".join([str(i) for i in list_credit_card]))
    return sum_of_digits(number) % 10 == 0


def main():
    credit_card = 79927398715
    print(is_credit_card_valid(credit_card))


if __name__ == '__main__':
    main()
