def search_in_dict(data, key, visited, structure, all_keys):
    for k, v in data.items():
        if k not in visited:
            visited.append((k, v))
            structure.append((k, v))
