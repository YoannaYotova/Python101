def gcd(nominator, denominator):
    if denominator != 0:
        while denominator != 0:
            temp = denominator
            denominator = nominator % denominator
            nominator = temp
        return nominator
    else:
        raise ZeroDivisionError('Cannot divide by zero')


def simplify_fraction(fraction):
    convert_to_list = list(fraction)

    common_dev = gcd(convert_to_list[0], convert_to_list[1])

    convert_to_list[0] = convert_to_list[0] // common_dev
    convert_to_list[1] = convert_to_list[1] // common_dev

    return tuple(convert_to_list)


def main():
    print(simplify_fraction((4, 10)))


if __name__ == '__main__':
    main()
