dic = {'a': '2',
       'b': '22',
       'c': '222',
       'd': '3',
       'e': '33',
       'f': '333',
       'g': '4',
       'h': '44',
       'i': '444',
       'j': '5',
       'k': '55',
       'l': '555',
       'm': '6',
       'n': '66',
       'o': '666',
       'p': '7',
       'q': '77',
       'r': '777',
       's': '7777',
       't': '8',
       'u': '88',
       'v': '888',
       'w': '9',
       'x': '99',
       'y': '999',
       'z': '9999',
       ' ': '0'}


def message_into_numbers(message):
    if len(message) == 0:
        raise ValueError('Empty message')

    new_list = []
    for i in range(0, len(message)):
        letter = message[i]
        if message[i].isupper():
                new_list.append(1)
                letter = message[i].lower()

        if i != (len(message) - 1) and len(dic[message[i].lower()]) <= len(dic[message[i + 1].lower()]) and dic[message[i].lower()][0] == dic[message[i + 1].lower()][0]:
            for x in dic[letter]:
                new_list.append(int(x))
            new_list.append(-1)
        elif letter in dic:
                for x in dic[letter]:
                    new_list.append(int(x))

    return new_list


def main():
    message = "Ivo e Panda"
    print(message_into_numbers(message))


if __name__ == '__main__':
    main()
