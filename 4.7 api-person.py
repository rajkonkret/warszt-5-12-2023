from pydantic import BaseModel
import requests as re

url = 'https://randomuser.me/api/'

response = re.get(url)
data = response.json()
print(response.text)
user = data['results'][0]
print(user)
print(f"Imię: {user['name']['first']}")
print(f"Nazwisko: {user['name']['last']}")
print(f"Email: {user['email']}")
photo_url = user['picture']['large']
response_photo = re.get(photo_url)
with open('user_photo.jpg', 'wb') as f:
    f.write(response_photo.content)

print("Zdjęcie zapisane")


# "name": {
#         "title": "Mr",
#         "first": "Tristan",
#         "last": "Taylor"
#       },
class Name(BaseModel):
    title: str
    first: str
    last: str


# "picture": {
#         "large": "https://randomuser.me/api/portraits/men/42.jpg",
#         "medium": "https://randomuser.me/api/portraits/med/men/42.jpg",
#         "thumbnail": "https://randomuser.me/api/portraits/thumb/men/42.jpg"
#       },
class Picture(BaseModel):
    large: str


class UserInfo(BaseModel):
    name: Name
    email: str
    picture: Picture


user_info = UserInfo(**user)
print(user_info)
print(type(user_info))  # <class '__main__.UserInfo'>

response_photo_pydantic = re.get(user_info.picture.large)
with open('user_photo_pydantic.jpg', 'wb') as f:
    f.write(response_photo_pydantic.content)

print("Zdjęcie pydantic zapisane")
