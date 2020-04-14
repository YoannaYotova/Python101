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
    finally:
        # print('In finally')
        getcontext().prec = 28
