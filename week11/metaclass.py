from class_decorator import debugmethods


class mymetaclass(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        # print('in my meta class')
        clsobj = debugmethods(clsobj)
        return clsobj


class Base(metaclass=mymetaclass):
    pass


class Panda(Base):
    def __init__(self, name):
        self.name = name

    def food(self):
        print('Bamboo')


class Dog(Base):
    def __init__(self, name):
        self.name = name

    def food(self):
        print('Socks')


if __name__ == '__main__':
    panda = Panda('Ani')
    panda.food()
    doggy = Dog('Archi')
    doggy.food()
