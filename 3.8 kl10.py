import pickle
from dataclasses import dataclass


# class Person:
#     def __init__(self, fn, ln, id):
#         self.fn = fn
#         self.ln = ln
#         self.id = id

@dataclass
class Person:
    first_name: str
    last_name: str
    id: int


pq1 = Person("Maciek", "nowak", 1)
print(pq1)  # Person(first_name='Maciek', last_name='nowak', id=1)
p2 = Person("Tomek", "kowalski", "2")
print(p2)  # Person(first_name='Tomek', last_name='kowalski', id='2')

people = [pq1, p2]
print(people)
# [Person(first_name='Maciek', last_name='nowak', id=1), Person(first_name='Tomek', last_name='kowalski', id='2')]

with open('dane.pickle', 'wb') as stream:
    pickle.dump(people, stream)
