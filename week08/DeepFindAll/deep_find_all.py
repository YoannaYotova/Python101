from utls import search_in_dict


def deep_find_all_dfs(data, key):
    all_keys = []
    stack = list(data.items())
    visited = []

    while len(stack) > 0:
        visited.append(stack[-1])
        node = stack[-1]
        stack.pop()
        # print(node)

        if node[0] == key:
            all_keys.append(node[1])
            
        # working with tuples
        # first element of the node is the key, second is the value
        if isinstance(node[1], dict):
            if isinstance(node[1], dict):
                search_in_dict(node[1], key, visited, stack, all_keys)

            elif isinstance(node[1], list):
                for element in node[1]:
                    if isinstance(element, dict):
                        search_in_dict(element, key, visited, stack, all_keys)
    
    return all_keys


def deep_find_all_bfs(data, key):
    all_keys = []
    queue = list(data.items())
    visited = []

    while len(queue) > 0:
        visited.append(queue[-1])
        node = queue[-1]
        queue.remove(node)
        
        if node[0] == key:
            all_keys.append(node[1])

        # working with tuples
        # first element of the node is the key, second is the value
        if isinstance(node[1], dict):
            if isinstance(node[1], dict):
                search_in_dict(node[1], key, visited, queue, all_keys)

            elif isinstance(node[1], list):
                for element in node[1]:
                    if isinstance(element, dict):
                        search_in_dict(element, key, visited, queue, all_keys)
    
    return all_keys