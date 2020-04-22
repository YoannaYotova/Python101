def deep_find(data, key):
    if key in data:
        return data[key]

    for k, v in data.items():
        if isinstance(v, dict):
            return deep_find(v, key)
        # not tested
        elif isinstance(v, list):
            for el in v:
                if isinstance(el, dict):
                    return deep_find(v, key)
