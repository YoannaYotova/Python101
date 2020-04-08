def chain(iterable_one, iterable_two):
    concatenated = []
    for el in iterable_one:
        concatenated.append(el)
    for el in iterable_two:
        concatenated.append(el)

    return concatenated


def compress(iterable, mask):
    res = []

    for index in range(len(mask)):
        if mask[index] is True:
            res.append(iterable[index])

    return res


def cycle(iterable):
    for x in iterable:
        yield x


def main():
    print(chain(range(0, 6), range(6, 8)))
    print(compress(['Anni', 'Pesho', 'Panda'], [True, False, True]))

    endless = cycle(range(0, 10))
    for item in endless:
        print(item)


if __name__ == '__main__':
    main()
