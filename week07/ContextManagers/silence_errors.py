from contextlib import contextmanager


@contextmanager
def silence_errors(exc_type, message=None):
    try:
        # print('In try')
        yield
    except Exception as exc:
        if not isinstance(exc, exc_type):
            raise exc

        if message is not None and str(exc) != message:
            raise exc


class SilenceErrors:
    def __init__(self, exc_type, message=None):
        self.exc_type = exc_type
        self.message = message

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.exc_type != exc_type:
            raise exc_type(exc_value)

        if self.message is not None and str(exc_value) != self.message:
            raise exc_type(exc_value)

        return True

        # better way to do this
        # same_exception_type = self.exc_type == exc_type
        # correct_message = self.msg is None or str(exc_value) == self.msg

        # return same_exception_type and correct_message
