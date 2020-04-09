def chain1(iterable_one, iterable_two):
    concatenated = []
    for el in iterable_one:
        concatenated.append(el)
    for el in iterable_two:
        concatenated.append(el)

    return concatenated


def chain2(iterable_one, iterable_two):
    return [*iterable_one, *iterable_two]


# chain as generator
def chain3(iterable_one, iterable_two):
    for el in iterable_one:
        yield el
    for el in iterable_two:
        yield el


def compress1(iterable, mask):
    res = []

    for index in range(len(mask)):
        if mask[index] is True:
            res.append(iterable[index])

    return res


# compress as generator
def compress2(iterable, mask):

    for index in range(len(mask)):
        if mask[index] is True:
            yield iterable[index]


def cycle(iterable):
    for x in iterable:
        yield x


def main():
    print("concatenate with chain1: ", chain1(range(0, 6), range(6, 8)))
    print("concatenate with chain2: ", chain1(range(3, 6), range(6, 10)))
    print("concatenate with chain3(generator): ", list(chain3(range(3, 7), range(7, 10))))
    print(compress1(['Anni', 'Pesho', 'Panda'], [True, False, True]))
    print(list(compress2(['Anni', 'Pesho', 'Panda'], [False, False, True])))

    endless = cycle(range(0, 10))
    for item in endless:
        print(item)


if __name__ == '__main__':
    main()
