# rest api - get, post, put/patch, delete, head
from pydantic import BaseModel
from typing import List
import requests as re

url = 'http://api.open-notify.org/astros.json'
# {"name":"Radek"} - json

# ppobieranie danych z api
response = re.get(url)
print(response)
# 200 <Response [200]> ok
# 3xx - błedy np.: przekierowania
# 4xx - 404 - błedy wyowłania po stronie uzytkownika, 400 Bad Request
# 5xx - błedy serwera. np problem z baza danych
print(response.text)  # wyswietla json
response_data = response.json()  # wyswietla słownik
print(response_data)
print(type(response_data))  # <class 'dict'>

for i in response_data:
    print(i)

for k, v in response_data.items():
    print(k, "=>", v)

for p in response_data['people']:
    print(p)


# {'name': 'Jasmin Moghbeli', 'craft': 'ISS'}
# {'name': 'Andreas Mogensen', 'craft': 'ISS'}
# {'name': 'Satoshi Furukawa', 'craft': 'ISS'}
# {'name': 'Konstantin Borisov', 'craft': 'ISS'}
# {'name': 'Oleg Kononenko', 'craft': 'ISS'}
# {'name': 'Nikolai Chub', 'craft': 'ISS'}
# {'name': "Loral O'Hara", 'craft': 'ISS'}

# {'name': 'Oleg Kononenko', 'craft': 'ISS'}
class Astronaut(BaseModel):
    name: str
    craft: str


class AstroData(BaseModel):
    message: str
    people: List[Astronaut]
    number: int
    # typy danych przy tym podejsciu są walidowane
    # number: str  #   Input should be a valid string [type=string_type, input_value=7, input_type=int]


data = AstroData(**response.json())
print(data)
# message = 'success'
# people = [Astronaut(name='Jasmin Moghbeli', craft='ISS'), Astronaut(name='Andreas Mogensen', craft='ISS'),
#           Astronaut(name='Satoshi Furukawa', craft='ISS'), Astronaut(name='Konstantin Borisov', craft='ISS'),
#           Astronaut(name='Oleg Kononenko', craft='ISS'), Astronaut(name='Nikolai Chub', craft='ISS'),
#           Astronaut(name="Loral O'Hara", craft='ISS')]
# number = 7
print(type(data))  # <class '__main__.AstroData'>
print(data.people)
for astronaut in data.people:
    print(f"{astronaut.name}, {astronaut.craft}")
# Jasmin Moghbeli, ISS
# Andreas Mogensen, ISS
# Satoshi Furukawa, ISS
# Konstantin Borisov, ISS
# Oleg Kononenko, ISS
# Nikolai Chub, ISS
# Loral O'Hara, ISS
