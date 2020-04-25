def generate_start(frogs):
    left_frogs = '>' * (frogs // 2)
    rigth_frogs = '<' * (frogs // 2)
    return f'{left_frogs}_{rigth_frogs}'


def generate_final(frogs):
    left_frogs = '<' * (frogs // 2)
    rigth_frogs = '>' * (frogs // 2)
    return f'{left_frogs}_{rigth_frogs}'


def legal_moves(position):
    lily = position.find('_')
    all_pos = []
    if lily - 1 >= 0 and position[lily - 1] == '>':
        swaped = list(position)
        swaped[lily - 1], swaped[lily] = swaped[lily], swaped[lily - 1]
        all_pos.append(''.join(swaped))
    if lily - 2 >= 0 and position[lily - 2] == '>':
        swaped = list(position)
        swaped[lily - 2], swaped[lily] = swaped[lily], swaped[lily - 2]
        all_pos.append(''.join(swaped))
    if lily + 1 < len(position) and position[lily + 1] == '<':
        swaped = list(position)
        swaped[lily + 1], swaped[lily] = swaped[lily], swaped[lily + 1]
        all_pos.append(''.join(swaped))
    if lily + 2 < len(position) and position[lily + 2] == '<':
        swaped = list(position)
        swaped[lily + 2], swaped[lily] = swaped[lily], swaped[lily + 2]
        all_pos.append(''.join(swaped))

    return all_pos


def solution(position, lily, end, stack=None):
    if position == end:
        print(end)
        return "SOLVED"
    else:
        if stack is None:
            stack = [position]
        else:
            stack.append(position)


def main():
    frogs = int(input('How many frogs are in the lake? '))

    print(generate_start(frogs))
    print(generate_final(frogs))


if __name__ == '__main__':
    main()
