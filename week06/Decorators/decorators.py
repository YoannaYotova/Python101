import time


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
        def write_in_file(*args, **kwargs):
            startTime = time.time()
            res = func(*args, **kwargs)
            endTime = time.time() - startTime

            with open(file_name, 'a') as f:
                f.write(f'get_low was called and took {endTime} seconds to complete\n')
            return res
        return write_in_file
    return inner_func


@performance('log.txt')
def something_heavy():
    time.sleep(2.10)
    return 'I am done!'


def silence(file_name):
    def inner_func(func):
        def take_the_errors(*func_arg):
            try:
                func(*func_arg)
            except Exception as err:
                arg = [i for i in func_arg]
                with open(file_name, 'a') as f:
                    f.write(f'Calling {func.__name__} raised an error - {type(err).__name__}: {err} Provided arguments: {tuple(arg)}\n')
        return take_the_errors
    return inner_func


@silence('errors.txt')
def foo(x):
    if x > 50:
        raise ValueError('Omg.')


def required(func):
    def checking_for_overriden_method(instance, *arg, **kwargs):
        if func.__name__ not in instance.__dict__:
            raise AttributeError(f'All classes that inherit from "{instance.__class__.__name__}" must provide "{func.__name__}" method')

        return func(instance, *arg, **kwargs)
    return checking_for_overriden_method


class Animal:
    @required
    def eat(self, food):
        print(food)


class Panda(Animal):
    # def eat(self, food):
    #     print('Panda eats: ', food)
    pass


def main():
    # deposit('Anni', 23)
    # print(say_hello('Anni'))
    # print(say_hello(4))

    # something_heavy()
    # foo(10)
    # foo(300)
    a = Panda()
    a.eat('bamboo')


if __name__ == '__main__':
    main()
