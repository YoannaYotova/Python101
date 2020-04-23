def search_in_dict(data, key, visited, structure):
    for k, v in data.items():
        if k not in visited:
            if k == key:
                return data[k]

            visited.append(k)
            structure.append(k)
