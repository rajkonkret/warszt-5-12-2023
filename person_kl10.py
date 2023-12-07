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


if __name__ == '__main__':
    print("Klasa Person")
