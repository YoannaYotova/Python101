def deep_compare(obj1, obj2):
    for k,v in obj1.items():
        if k not in obj2:
            return False
        else:
            if isinstance(v, dict):
                return deep_compare(v, obj2[k])
            else:
                if v != obj2[k]:
                    # print('IN FALLSE', k, v)
                    return False

    return True