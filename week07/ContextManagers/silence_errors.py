from contextlib import contextmanager


@contextmanager
def silence_errors(exc_type, message=None):
    try:
        # print('In try')
        yield
    except Exception as exc:
        if not isinstance(exc, exc_type):
            raise exc


with silence_errors(TypeError):
    print('In with block')
    raise ValueError('Test')
