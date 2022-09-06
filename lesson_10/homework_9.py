import functools


class UnexpectedTypeException(Exception):
    def __init__(self, types):
        types_text = ""
        for type_desc in types:
            types_text = types_text + type_desc.__name__ + ', '
        types_text = types_text[:-2]
        self.message = "Was expecting types: " + types_text
        super().__init__(self.message)


def expected(*typeargs):
    def decorator_expected(func):
        @functools.wraps(func)
        def wrapper_expected(*args, **kwargs):
            flag = False
            largs = list(args)
            for types in typeargs:
                current_arg = largs.pop(0)
                for type_desc in types:
                    if type(current_arg) == type_desc:
                        flag = True
                        break
                if not flag:
                    raise UnexpectedTypeException(types)
                flag = False
            return func(*args, **kwargs)
        return wrapper_expected
    return decorator_expected


@expected((int, str), (int,))
def func(value, i):
    print(value + str(i))


func("Who lets the dogs out", 1)