# api
from pprint import pprint
from typing import List

from pydantic import BaseModel
import requests as re

url = 'https://restcountries.com/v3.1/name/Poland'

response = re.get(url)
data = response.json()
print(response.text)
print(data)  # <class 'list'>

print(type(data))
print(data[0].keys())
country = data[0]
print(country['name'])
print(country['name']['common'])
print(country['name']['official'])
print("Stolica kraju", country['capital'][0])  # Stolica kraju Warsaw
print(country['population'])  # 37950802


# "nativeName": {
#         "pol": {
#           "official": "Rzeczpospolita Polska",
#           "common": "Polska"
#         }

class Pol(BaseModel):
    official: str
    common: str


class NativeName(BaseModel):
    pol: Pol


class Name(BaseModel):
    common: str
    official: str
    # nativeName: dict
    nativeName: NativeName


class CountryInfo(BaseModel):
    name: Name
    capital: List[str]
    population: int


country_data = [CountryInfo(**data) for data in response.json()]
print(country_data)
pprint(country_data)
# [CountryInfo(name=Name(common='Poland', official='Republic of Poland',
#                        nativeName={'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}),
#              capital=['Warsaw'], population=37950802)]
print(type(country_data[0]))  # <class '__main__.CountryInfo'>
for country in country_data:
    print(f'{country.name}, {country.capital} {country.name.nativeName.pol.official}')
# 13:25
