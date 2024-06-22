import requests
import json
from bs4 import BeautifulSoup

def search_last_page(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')

    last_page = soup.find('li', class_='pagination__item ng-star-inserted').text.strip()
    return int(last_page)

def get_all_ads(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')

    ads = soup.find_all('div', class_='goods-tile__inner')
    return ads

def get_description_ad(ads):
    list_descript = list()

    for i in ads:
        descript = dict()
        descript['name'] = i.find('span', class_='goods-tile__title').text
        descript['new_price'] = i.find('span', class_='goods-tile__price-value').text
        descript['url'] = i.find('a', class_='product-link goods-tile__heading').get('href')

        resp = requests.get(descript['url'])
        soup = BeautifulSoup(resp.text, 'lxml')

        descript['description'] = soup.find('p', class_='mt-4 ng-star-inserted').text
        list_descript.append(descript)
    return list_descript

def main():
    first_url = 'https://rozetka.com.ua/ua/news-articles-promotions/promotions/232592_delivery_bf_laptops/'
    last_page = search_last_page(first_url)

    for i in range(1, last_page + 1):
        url = f'{first_url}page={i}/'
        ads = get_all_ads(url)
        desc = get_description_ad(ads)

        with open(f"web_scraping\\4st_practice\\data1.json", "a", encoding='UTF-8') as file:
            json.dump(desc, file, ensure_ascii=False)

if __name__ == '__main__':
    main()