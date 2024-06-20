import math
import requests
from bs4 import BeautifulSoup as bs

# Шукаємо кол-во сторінок
def count_all_pages(url):
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    find_all_ads = soup.find('span', class_='css-7ddzao')
    all_ads = find_all_ads.text.split()[2]
    return math.ceil(int(all_ads) / 35)

# Анализуємо пропозиції та витягуємо данні
def get_ads_on_first_page(url, page):
    url = f'https://www.olx.ua/uk/nedvizhimost/kvartiry/prodazha-kvartir/dnepr/?currency=UAH&page={page}&search%5Bdistrict_id%5D=111&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=odnokomnatnye'
    list_ads = list()
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    find_ads_first_page = soup.find_all('div', class_='css-qfzx1y')
    for i in find_ads_first_page:
        if 'ТОП' not in i.text:
            name_ad = i.find('h6', class_='css-16v5mdi er34gjf0')
            locat_date_ad = i.find('p', class_='css-1a4brun er34gjf0')
            price_ad = i.find('p', class_='css-tyui9s er34gjf0')
            get_class_link = i.find('a', class_='css-z3gu2d')
            link_ads = get_class_link.get('href')
            # Витягуємо опис квартири, та ціну в USD
            response_ad = requests.get(f'https://olx.ua{link_ads}')
            soup_ad = bs(response_ad.text, 'lxml')
            descrip_ad = soup_ad.find('div', class_='css-1t507yq er34gjf0')
            price_usd = soup_ad.find('h3', class_='css-12vqlj3')
            # Створюємо вигляд пропозиції(назва, посилання, локація, опис, валюта)
            values = (f'{name_ad.text}\n'
                      f'{locat_date_ad.text}\n'
                      f'\n'
                      f'Опис:\n{descrip_ad.text}\n'
                      f'https://olx.ua{link_ads}\n'
                      f'\n'
                      f'{price_ad.text} або {price_usd.text}\n')
            list_ads.append(values)
    return list_ads

# Проходимо по всім сторінкам і записуємо у файл
def ads_on_all_pages(url):
    pages = count_all_pages(url)
    
    for page in range(1, pages + 1):
        print(f'Аналізую {page} сторінку')
        list_ads_urls = get_ads_on_first_page(url, page)
        for i in list_ads_urls:
            with open('web_scraping\\second_homework\\OLX.txt', 'a', encoding='utf-8') as file:
                file.write(f'******************\n')
                file.write(i)
        print(f'Парсинг сторінки {page} завершено!')
    print(f'Парсинг завершенно!')
            
def main():
    url = f'https://www.olx.ua/uk/nedvizhimost/kvartiry/prodazha-kvartir/dnepr/?currency=UAH&search%5Bdistrict_id%5D=111&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=odnokomnatnye'
    ads_on_all_pages(url)
    

if __name__ == '__main__':
    main()