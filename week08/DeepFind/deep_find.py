from utls import search_in_dict


def deep_find(data, key):
    if key in data:
        return data[key]

    for k, v in data.items():
        if isinstance(v, dict):
            res = deep_find(v, key)
            if res is not None:
                return res

        elif isinstance(v, list):
            for el in v:
                if isinstance(el, dict):
                    res = deep_find(el, key)
                    if res is not None:
                        return res

    return None


# DFS
def deep_find_dfs(data, key):
    stack = list(data.items())
    visited = []

    while len(stack) > 0:
        visited.append(stack[-1])
        node = stack[-1]
        stack.pop()

        # working with tuples
        # first element of the nodi is key, second is the value
        if node[0] == key:
            return node[1]

        if isinstance(node[1], dict):
            res = search_in_dict(node[1], key, visited, stack)
            if res is not None:
                return res

        elif isinstance(node[1], list):
            for element in node[1]:
                if isinstance(element, dict):
                    res = search_in_dict(element, key, visited, stack)
                    if res is not None:
                        return res


# BFS
def deep_find_bfs(data, key):
    queue = list(data.items())
    visited = []

    while len(queue) > 0:
        visited.append(queue[0])
        node = queue[0]
        queue.remove(node)

        # working with tuples
        # first element of the nodi is key, second is the value
        if node[0] == key:
            return node[1]

        if isinstance(node[1], dict):
            res = search_in_dict(node[1], key, visited, queue)
            if res is not None:
                return res

        elif isinstance(node[1], list):
            for element in node[1]:
                if isinstance(element, dict):
                    res = search_in_dict(element, key, visited, queue)
                    if res is not None:
                        return res
