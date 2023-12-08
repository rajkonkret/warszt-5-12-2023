from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.pracuj.pl/praca/programista%20python;kw'
# url = 'https://justjoin.it'
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")
# print(soup)

data = soup.find('script', {'id': '__NEXT_DATA__'}).text
# print(data)
offers_count = int(data.split('offersCount":')[1].split(",")[0])
print(offers_count)  # 592
# 15:05
