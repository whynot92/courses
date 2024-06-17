import requests
from bs4 import BeautifulSoup

page_number = 1
number_pages = list()

url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page_number}'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')

action = soup.find_all('a', class_='title')
price = soup.find_all('h4', class_='price float-end card-title pull-right')
pages = soup.find('ul', class_='pagination')

for i in pages.text.split('\n'):
    if i.isalnum():
        number_pages.append(i)
with open('price.txt', 'a') as f:
    while page_number < int(number_pages[-1]) + 1:
        print('-' * 70)
        print(f'Страница № {page_number}')
        print('-' * 70)
        for a, p in zip(action, price):
            links = a.get('href')
            print('\n')
            print(f'Ноутбук: {a.text}')
            print(f'Цена: {p.text}')
            print(f'https://webscraper.io/{links}')
            print('\n')
            print('*' * 20)
        page_number += 1
    
    else:
        print('-' * 70)
        print('End price')
        print('-' * 70)


