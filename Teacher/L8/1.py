import requests
from bs4 import BeautifulSoup as bs
import math
from pprint import pprint

def get_count_ads_for_page(url):
    responce = requests.get(url)
    soup = bs(responce.text, 'lxml')
    ads = soup.find_all('div', class_='css-qfzx1y')
    count = 0
    for i in ads:
        find_top = i.find('div', class_='css-13aawz3')
        if "ТОП" not in find_top.text:
            count += 1
    print(f'Количество объявлений на странице: {count}')

def get_count_pages(url):
    responce = requests.get(url)
    soup = bs(responce.text, 'lxml')
    pages = soup.find('span', class_='css-7ddzao')
    pages = pages.text.split()[2]
    return math.ceil(int(pages)/40)

def get_ads_urls(url, page):
    url = f'{url}?page={page}'
    responce = requests.get(url)
    soup = bs(responce.text, 'lxml')
    ads = soup.find_all('div', class_='css-qfzx1y')
    list_url_ads = []
    for i in ads:
        find_top = i.find('div', class_='css-13aawz3')
        if "ТОП" not in find_top.text:
            list_url_ads.append(i.find('a')['href'])

    return list_url_ads

def get_ads_data(url):
    ...



def main():
    url = 'https://www.olx.ua/uk/list/q-thinkpad-x280/'
    count_page = get_count_pages(url)

    for page in range(1, count_page + 1):
        list_ads_urls = get_ads_urls(url, page)
        pprint(list_ads_urls)
        


if __name__ == '__main__':
    main()