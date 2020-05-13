class Positive:
    def __init__(self, value=None, name='var'):
        self.value = value
        self.name = name

    def __get__(self, instance, owner):
        if self.value is not None:
            print('Get: ', self.name)
            return self.value
        raise ValueError('No variable')

    def __set__(self, instance, val):
        if val < 0:
            raise ValueError('No negative integers')
        else:
            print('Update: ', self.name)
            self.value = val

    def __delete__(self, instance):
        print('Delete: ', self.name)
        del self.name


class PositiveInteger:
    x = Positive(3, 'var "x"')
    y = Positive()
