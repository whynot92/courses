import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

responce = requests.get(url)

if responce.status_code != 200:
    print(f'Error: {responce.status_code}')
    exit(0)

soup = BeautifulSoup(responce.text, 'lxml')

# phones = soup.find('a', class_='title')
# print(phones.text)

phones = soup.find_all('a', class_='title')
prices = soup.find_all('h4', class_='price')

data = dict(zip(phones, prices))

for phone, price in data.items():
    print(phone.text, price.text)



# for phone in phones:
#     print(phone.text)

# for price in prices:
#     print(price.text)