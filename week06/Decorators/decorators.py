import time
import datetime


def accepts(*types_of_arg):
    def inner_func(func):
        def check_for_right_arg(*func_arg):
            print('IN RIGTH ARG')
            decorator_types = [x for x in types_of_arg]

            for index in range(0, len(func_arg)):
                if type(func_arg[index]) is not decorator_types[index]:
                    raise ValueError(f'Argument is not {types_of_arg[index].__name__}')
            return func(*func_arg)
        return check_for_right_arg
    return inner_func


@accepts(str)
def say_hello(name):
    return f'Hello, I am {name}'


@accepts(str, int)
def deposit(name, money):
    print(f'{name} sends {money} $')


def performance(file_name):
    def inner_func(func):
        def write_in_file():
            startTime = datetime.datetime.now()
            func()
            endTime = datetime.datetime.now()
            elapsedTime = endTime - startTime
            with open(file_name, 'a') as f:
                f.write(f'get_low was called and took {str(elapsedTime)[5:10]} seconds to complete\n')
            return func()
        return write_in_file
    return inner_func


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return 'I am done!'


def main():
    # deposit('Anni', 23)
    # print(say_hello('Anni'))
    # print(say_hello(4))

    print(something_heavy())


if __name__ == '__main__':
    main()
