def removing_double_slash(path):
    reduced_file_path = ""
    if len(path) == 0:
        raise ValueError('Invalid path')

    for i in range(0, len(path) - 1):
        if path[i] != path[i + 1] or path[i] != "/":
            reduced_file_path += "".join(path[i])

    reduced_file_path = reduced_file_path + path[-1]
    return reduced_file_path


def removing_last_slash(path):
    if len(path) > 1 and path[-1] == "/":
        return path[:-1]
    else:
        return path


def removing_double_dots(path):
    path = removing_last_slash(path)
    path_in_list = path.split("/")
    path_in_list = [el for el in path_in_list if el != ""]

    for index, element in enumerate(path_in_list):
        if element == "..":
            del path_in_list[index - 1]

    new_path = "/".join(x for x in path_in_list if x != "..")
    return "/" + new_path


def removing_directory_point(path):
    path = path.replace("./", "")
    path = removing_last_slash(path)
    return path


def main():
    path = "/etc/../etc/../etc/../"
    path = removing_double_slash(path)
    path = removing_double_dots(path)
    path = removing_directory_point(path)

    print(path)


if __name__ == '__main__':
    main()
