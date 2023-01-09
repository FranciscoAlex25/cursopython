def return_string(func):
    def is_string(*args):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError('O valor informado não é str')
        print('String invertida')
        return func(*args)
    return is_string


@return_string
def inverter(string):
    return string[::-1]


# string = return_string(inverter)

print(inverter('alex'))
