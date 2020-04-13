from contextlib import contextmanager
from decimal import *


class ChangePrecision:
    def __init__(self, num):
        self.num = num

    def __enter__(self):
        getcontext().prec = self.num
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        getcontext().prec = 28


@contextmanager
def change_precision(num):
    try:
        # print('In try')
        getcontext().prec = num
        yield
    except Exception:
        # print('In except')
        pass
    else:
        # print('In else')
        pass
    finally:
        # print('In finally')
        getcontext().prec = 28
        pass


# with change_precision(2):
#     print(Decimal('1.123132132') + Decimal('2.23232'))


# print(Decimal('1.123132132') + Decimal('2.23232'))
