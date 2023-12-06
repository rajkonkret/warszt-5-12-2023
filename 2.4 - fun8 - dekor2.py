# dekorator który zmienia tekst na duże litery
def uppeercase_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m" + result + "\033[0m"

    return wrapper


@uppeercase_decorator  # uzycie dekarotara na funkcji
def greeting():
    return "Hello World!"


@bold_decorator
@uppeercase_decorator
def greeting2(name):
    return name


# print(greeting())
# Hello World!
# po dodaniu dekoratora
# HELLO WORLD!
print(greeting2("Radek"))
