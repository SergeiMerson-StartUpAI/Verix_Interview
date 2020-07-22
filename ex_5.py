import random


def ext_load_data_func(path_to_file):
    value = random.randint(1, 100)
    if value > 75:
        raise FileNotFoundError()
    return value

def ext_process_value_func(value):
    errors = {
        1: ValueError,
        2: TypeError,
        3: KeyError,
        4: ZeroDivisionError
    }
    multiplyer = random.randint(1, 25)
    if multiplyer in errors:
        raise errors[multiplyer]
    return multiplyer * value
