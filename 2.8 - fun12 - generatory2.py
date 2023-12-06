generator_1 = [x for x in range(5)]
print(generator_1)
print(type(generator_1))  # <class 'list'>

generator2 = (x for x in [1, 2, 3, 4, 5])
print(type(generator2))  # <class 'generator'>
print(next(generator2))
print(next(generator2))
print(next(generator2))
print(next(generator2))
print(next(generator2))


# print(next(generator2))  # StopIteration

def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))


def gen4():
    i = 1
    while True:
        yield i * 1
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fi = fibo()
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fino2 = fibo_with_index(100)
print(next(fino2))
print(next(fino2))
print(next(fino2))
print(next(fino2))
print(next(fino2))
print(next(fino2))
print(next(fino2))

# to są dwa rózne generatory
for i in fibo_with_index(10):
    print(f"Element {i}")  # Element (9, 34)

for i, n in fibo_with_index(10):
    print(f"Pozycja {i}, elemnt {n}")  # Pozycja 0, elemnt 0

fibo3 = fibo_with_index(10)
# print(list(fibo3))  # zrzutowanie danych generatora na liste wyczerpuje jego zakres
print("---------")
for i in fibo3:
    print(i)


# print(next(fibo3))  # StopIteration
# 13:30

def counter(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break
        n += 1


c = counter(10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(c.send("Ok"))  # Ok
try:
    c.send('q')  # StopIteration
except StopIteration:
    pass

print(next(c))  # StopIteration
