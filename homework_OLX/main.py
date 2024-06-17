import requests
from bs4 import BeautifulSoup

number_page = 1
url = 'https://www.olx.ua/uk/list/q-thinkpad-x280/?page={number_page}'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

links = soup.find_all('div', class_='css-qfzx1y')


if resp.status_code == 200:
    print('\n')
    print('-' * 70)
    print(f'Страница {number_page}')
    print('-' * 70)

    for i in links:
 
        link = i.find_all('a', class_='css-z3gu2d')
        prace = i.find_all('p', class_='css-tyui9s er34gjf0')
        name = i.find_all('h6', class_='css-16v5mdi er34gjf0')
        for a, b, c in zip(name, link, prace):
            article_link = b.get('href')
            print('\n')
            print(a.text)
            print(f'Цена: {c.text}')
            print(f'Ссылка: https://olx.ua{article_link}')

    print('\n')
    print('-' * 70)
    print(f'Страница {number_page + 1}')
    print('-' * 70)
    print('\n')


else:
    print(f"Не удалось получить доступ к странице")

