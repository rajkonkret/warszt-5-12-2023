from bs4 import BeautifulSoup
import requests

url = "https://wowpedia.fandom.com/wiki/Zul%27jin"

soup = BeautifulSoup(requests.get(url).content, "html.parser")
# print(soup)

table = soup.find('table', class_="infobox darktable")
# print(table)

for tag in table.find_all(class_="reference"):
    tag.decompose()
print(table)

for th in table.find_all("th")[1:]:
    print(f"{th.text}: {th.next_sibling.get_text(strip=True)}")
# Title: Warlord of Zul'Aman,Chieftainof the Amani
# Gender: Male
# Race: Forest troll(Undead)
# Class: Warrior
# Reaction: AllianceHorde
# Former affiliation(s): Amani tribe,Old Horde,Revantusk tribe
# Former occupation(s): Axe thrower, Ruler of the Amani tribe andZul'Aman
# Location: Various
# Status: Deceased
