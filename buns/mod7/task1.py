def validate_args(func):
    def wrapper_func(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "too many arguments"
        elif not isinstance(args[0], int):
            return "wrong types"
        elif args[0] < 0:
            return "negative argument"
        else:
            return func(*args)
    return wrapper_func


@validate_args
def example_func(x):
    return x


print(example_func(1))
print(example_func())
print(example_func(1, 1))
print(example_func(-4))
