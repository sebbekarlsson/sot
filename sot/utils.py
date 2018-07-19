class Struct(object):

    def __init__(self, **entries):
        self.__dict__.update(entries)


def try_except(success, exception, error, args={}):
    try:
        return success(Struct(**args))
    except exception as e:
        return error(e)


def loop(expression, func):
    while expression:
        func()
