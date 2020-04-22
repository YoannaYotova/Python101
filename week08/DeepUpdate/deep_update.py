def deep_update(data, key, val):
    if key in data:
        data[key] = val

    for k, v in data.items():
        if isinstance(v, dict):
            deep_update(v, key, val)
        elif isinstance(v, list):
            for el in v:
                if isinstance(el, dict):
                    deep_update(el, key, val)

    return data
