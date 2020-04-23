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
            for k, v in data[node].items():
                if k not in visited:
                    # print(k)
                    if k == key:
                        # print(data[node][k])
                        return data[node][k]

                    visited.append(k)
                    stack.append(k)

        elif isinstance(data[node], list):
            for element in data[node]:
                if isinstance(element, dict):
                    for k, v in element.items():
                        if k not in visited:
                            if k == key:
                                return element[k]

                            visited.append(k)
                            stack.append(k)


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
            for k, v in data[node].items():
                if k not in visited:
                    # print(k)
                    if k == key:
                        # print(data[node][k])
                        return data[node][k]

                    visited.append(k)
                    queue.append(k)

        elif isinstance(data[node], list):
            for element in data[node]:
                if isinstance(element, dict):
                    for k, v in element.items():
                        if k not in visited:
                            if k == key:
                                return element[k]

                            visited.append(k)
                            queue.append(k)
