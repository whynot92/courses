import requests
from bs4 import BeautifulSoup

url = 'https://www.olx.ua/uk/elektronika/telefony-i-aksesuary/?currency=UAH&search%5Border%5D=created_at%3Adesc'

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'lxml')

items = soup.find_all('h6', class_='css-16v5mdi er34gjf0')

for i in items:
    print(i.text)
