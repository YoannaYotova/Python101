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
def deep_find2(data, key):
    stack = list(data.keys())
    visited = []

    while len(stack) > 0:
        visited.append(stack[-1])
        node = stack[-1]
        stack.pop()

        if node == key:
            return data[node]

        if isinstance(data[node], dict):
            res = search_in_dict(data[node], key, visited, stack)
            if res is not None:
                return res

        elif isinstance(data[node], list):
            for element in data[node]:
                if isinstance(element, dict):
                    res = search_in_dict(element, key, visited, stack)
                    if res is not None:
                        return res


# BFS
def deep_find3(data, key):
    queue = list(data.keys())
    visited = []

    while len(queue) > 0:
        visited.append(queue[0])
        node = queue[0]
        queue.remove(node)

        if node == key:
            return data[node]

        if isinstance(data[node], dict):
            res = search_in_dict(data[node], key, visited, queue)
            if res is not None:
                return res

        elif isinstance(data[node], list):
            for element in data[node]:
                if isinstance(element, dict):
                    res = search_in_dict(element, key, visited, queue)
                    if res is not None:
                        return res
