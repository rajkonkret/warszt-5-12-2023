# oddziela argumenty pozycyjne od nazwanych
def example(a, b, /, d=0, **kwargs):  # ** argumenty słownikowe
    print("a, b", a, b)
    print("d", d)
    print("kwargs", kwargs)


example(1, 2)
# po dodaniu / w argumentach a i b nie mogą zostac wywolane po nazwie
# example(b=1, a=2)
# TypeError: example() got some positional-only arguments passed as keyword arguments: 'a, b'
example(1, 2, 4)
example(1, 2, d=5)
# example(1, 2, d=5, a=8)  # TypeError: example() got some positional-only arguments passed as keyword arguments: 'a'
example(1, 2, d=5, a=8)  # kwargs {'a': 8}


def all_params(*args, **kwargs):  # pryjmie i pozycyjne i po nazwie
    print(args, kwargs)


all_params(1, a=8)  # (1,) {'a': 8}
print(example.__code__.co_varnames)  # ('a', 'b', 'd', 'kwargs')
print(all_params.__code__.co_varnames)  # ('args', 'kwargs')
