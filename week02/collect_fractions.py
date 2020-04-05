from simplify_fraction import simplify_fraction, gcd


def sum_of_two_fractions(frac1, frac2):
    denominator = gcd(frac1[1], frac2[1])

    denominator = (frac1[1] * frac2[1]) // denominator

    nominator = (frac1[0] * (denominator // frac1[1]) + frac2[0] * (denominator // frac2[1]))

    res = simplify_fraction((nominator, denominator))
    if str(res) == 'Cannot divide by zero':
        raise ZeroDivisionError('Cannot divide by zero')
    else:
        return res


def collect_fractions(fractions):
    convert_to_list = list(fractions)
    first_fraction = convert_to_list[0]
    for i in range(1, len(convert_to_list)):
        first_fraction = sum_of_two_fractions(first_fraction, convert_to_list[i])
    return first_fraction


def main():
    print(collect_fractions([(1, 7), (2, 6)]))


if __name__ == '__main__':
    main()
