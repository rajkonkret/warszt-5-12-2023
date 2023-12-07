class Count:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


counter = Count(1, 5)
while True:
    try:
        number = next(counter)
        print(number)
    except StopIteration:
        break

counter2 = Count(1, 10)
print(next(counter2))
print(next(counter2))
print(next(counter2))
