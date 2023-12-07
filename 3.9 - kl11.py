import pickle
from person_kl10 import Person
from dataclasses import dataclass

# mozemy ta klase zaimportowac z właściwego pliku
# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     id: int


with open('dane.pickle', 'rb') as file:
    p = pickle.load(file)

print("--------")
print(p)
# [Person(first_name='Maciek', last_name='nowak', id=1),
# Person(first_name='Tomek', last_name='kowalski', id='2')]
for person in p:
    print(f"id={person.id}, first name={person.first_name} last name: {person.last_name}")
# id=1, first name=Maciek last name: nowak
# id=2, first name=Tomek last name: kowalski
