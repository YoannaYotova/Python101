from functools import wraps

def debug(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    for key, value in vars(cls).items():
        if not key.startswith('__') and callable(value):
            # must be set!!!
            # value = debug(value)
            setattr(cls, key, debug(value))

    return cls


@debug
def foo():
    print('here')


@debugmethods
class Panda:
    def food(self):
        print('Bamboo')

    def sleep(self):
        print('24/7')


if __name__ == '__main__':
    # foo()
    panda = Panda()
    panda.food()
    panda.sleep()
