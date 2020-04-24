def func(key=None):
    return str(key) + '_new'


def deep_apply(func, data):
    for k in list(data):
        if isinstance(data[k], dict):
            new_val = deep_apply(func, data[k])
            data[k] = new_val

        elif isinstance(data[k], list):
            for el in data[k]:
                if isinstance(el, dict):
                    deep_apply(func, el)

        if '_new' not in str(k):
            data[func(k)] = data.pop(k)
    return data
