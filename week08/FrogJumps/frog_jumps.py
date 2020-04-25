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


def solution(position, end, path=[]):
    # print('path', path)
    cur_path = path + [position]
    # print('cur_path', cur_path)
    if position == end:
        return cur_path
    moves = legal_moves(position)

    if len(moves) == 0:
        return None

    for node in moves:
        if node not in cur_path:
            new_path = solution(node, end, cur_path)
            if new_path:
                return new_path

    return None


def main():
    frogs = int(input('How many frogs are in the lake? '))

    right_path = solution(generate_start(frogs), generate_final(frogs))
    print('Right Path')
    for step in right_path:
        print(step)


if __name__ == '__main__':
    main()
