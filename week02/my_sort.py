def my_sort(iterable=None, ascending=True, key=None):
    if iterable == () or iterable == []:
        return iterable

    elif iterable is not None:

        # converting the tuple into list ( cannot change a tuple)
        if type(iterable) == tuple:
            converted_iterable = list(iterable)
        else:
            converted_iterable = iterable

        # in this case we work with dictionaries
        if type(converted_iterable[0]) == dict:

            for i in range(0, len(converted_iterable) - 1):
                for j in range(i + 1, len(converted_iterable)):
                    if converted_iterable[i][key] > converted_iterable[j][key]:
                        converted_iterable[i], converted_iterable[j] = converted_iterable[j], converted_iterable[i]

            if ascending is False:
                converted_iterable.reverse()
            return converted_iterable

        # in this case we work with list
        else:
            new_iterable = []
            for x in range(len(converted_iterable)):
                new_iterable.append(min(converted_iterable))
                converted_iterable.remove(min(converted_iterable))

            if ascending is False:
                new_iterable.reverse()

            if type(converted_iterable) != type(iterable):
                return (type(iterable))(new_iterable)
            else:
                return new_iterable

    else:
        raise ValueError('Calling the function with no arguments.')


def main():
    print(my_sort([2, 3, 12, 34], False))


if __name__ == '__main__':
    main()
