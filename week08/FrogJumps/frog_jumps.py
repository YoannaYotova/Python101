def generate_start(frogs):
    left_frogs = '>' * (frogs // 2)
    right_frogs = '<' * (frogs // 2)
    return f'{left_frogs}_{right_frogs}'


def generate_end(frogs):
    left_frogs = '<' * (frogs // 2)
    right_frogs = '>' * (frogs // 2)
    return f'{left_frogs}_{right_frogs}'


def move_frog(path, frog_position, lily_position):
    current_pos = list(path)
    current_pos[frog_position], current_pos[lily_position] = current_pos[lily_position], current_pos[frog_position]
    return ''.join(current_pos)


def possible_moves(position):
    lily = position.find('_')
    all_pos = []
    if lily - 1 >= 0 and position[lily - 1] == '>':
        movement = move_frog(position, lily - 1, lily)
        all_pos.append(movement)

    if lily - 2 >= 0 and position[lily - 2] == '>':
        movement = move_frog(position, lily - 2, lily)
        all_pos.append(movement)

    if lily + 1 < len(position) and position[lily + 1] == '<':
        movement = move_frog(position, lily + 1, lily)
        all_pos.append(movement)

    if lily + 2 < len(position) and position[lily + 2] == '<':
        movement = move_frog(position, lily + 2, lily)
        all_pos.append(movement)

    return all_pos


def find_path(position, end, path=None):
    if path is None:
        path = []

    current_path = path[:]
    current_path.append(position)

    if position == end:
        return current_path
    moves = possible_moves(position)

    if len(moves) == 0:
        return None

    for node in moves:
        if node not in current_path:
            new_path = find_path(node, end, path=current_path)
            if new_path:
                return new_path

    return None


def main():
    frogs = int(input('How many frogs are in the lake? '))
    start = generate_start(frogs)
    end = generate_end(frogs)
    right_path = find_path(start, end)
    print('Right Path')
    for step in right_path:
        print(step)


if __name__ == '__main__':
    main()
